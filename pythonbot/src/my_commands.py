import asyncio

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandObject, Filter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from db_operations import add_fav_group, get_group_number, get_all_users
from fsm import DayState
from keyboards import get_days_keyboard, get_my_group_schedule
from misc import create_text_schedule
from parsing import get_group_id, get_group_schedule_current_week

my_router = Router(name=__name__)


@my_router.message(Command('add'))
async def command_add_group_handler(message: Message, command: CommandObject) -> None:
    group_name = command.args
    if group_name is None:
        await message.answer('Вы не ввели название группы.\n/add 505/5  - (пример)')
        return

    group_id = get_group_id(group_name)

    if group_id is None:
        await message.answer('Такой группы не существует')
        return

    add_fav_group(message.from_user.id, group_id)
    await message.answer('Группа успешно добавлена в избранное.')


@my_router.message(F.text == 'Мое расписание')
async def command_my_fav_group_schedule_handler(message: Message, state: FSMContext) -> None:
    group_id = get_group_number(message.from_user.id)
    if group_id is None:
        await message.answer('Error')
        return

    await message.answer('Выберите день недели', reply_markup=get_days_keyboard())
    await state.set_state(DayState.day)


@my_router.message(DayState.day)
async def process_day(message: Message, state: FSMContext) -> None:
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Все дни']
    group_id = get_group_number(message.from_user.id)
    data = message.text
    await state.clear()
    if data not in days:
        await message.answer('Такой вариант я не предлагал', reply_markup=get_my_group_schedule())
        return
    if data == days[-1]:
        schedule = get_group_schedule_current_week(group_id)
        for day in days[:-1]:
            await message.answer(f"{create_text_schedule(schedule, day)}", reply_markup=get_my_group_schedule())
            await asyncio.sleep(1)
        return
    schedule = get_group_schedule_current_week(group_id)
    await message.answer(f"{create_text_schedule(schedule, data)}", reply_markup=get_my_group_schedule())


class AdminFilter(Filter):
    def __init__(self) -> None:
        self.admins_ids = [123]

    async def __call__(self, message: Message) -> bool:
        return True
        return message.from_user.id in self.admins_ids


@my_router.message(Command('stats'), AdminFilter())
async def command_stats_group_handler(message: Message) -> None:
    all_users = get_all_users()
    count_users = len(all_users)
    await message.answer(f'кол-во пользователей сейчас: {count_users}')


@my_router.message(Command('send'), AdminFilter())
async def command_send_group_handler(message: Message, command: CommandObject, bot: Bot) -> None:
    all_users = get_all_users()

    send_text = command.args
    if send_text is None:
        await message.answer('Вы не ввели текст для рассылки')
        return

    for user in all_users:
        try:
            await bot.send_message(user[0], send_text)
        except:
            await message.answer('Юзер удалил чат')
