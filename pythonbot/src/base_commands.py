import asyncio

from aiogram import Router, types, Bot
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from db_operations import register_user, check_group_number_set
from fsm import ReportState
from keyboards import get_my_group_schedule
from misc import create_text_schedule
from parsing import get_group_schedule_current_week, get_group_id
from settings import admin_ids

base_router = Router(name=__name__)


def get_start_text():
    with open('start.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    return text


@base_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    telegram_id = message.from_user.id
    register_user(telegram_id)

    if check_group_number_set(telegram_id):
        await message.answer(f"{get_start_text()}", reply_markup=get_my_group_schedule())
        return
    await message.answer(f"{get_start_text()}")


@base_router.message(Command('report'))
async def command_report_handler(message: Message, state: FSMContext) -> None:
    await message.answer('Введите ваше сообщение:')
    await state.set_state(ReportState.report_message)


@base_router.message(ReportState.report_message)
async def process_report_message(message: Message, state: FSMContext, bot: Bot) -> None:
    for tg_id in admin_ids:
        await bot.send_message(tg_id, f'Пришло сообщение: {message.text}')
    await state.clear()


@base_router.message(Command('current'))
async def command_current_handler(message: Message, command: CommandObject) -> None:
    group_name = command.args
    if group_name is None:
        await message.answer('Вы не ввели название группы.\n/current 505/5  - (пример)')
        return

    group_id = get_group_id(group_name)

    if group_id is None:
        await message.answer('Такой группы не существует')
        return

    schedule = get_group_schedule_current_week(group_id)
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    for day in days:
        await message.answer(f"{create_text_schedule(schedule, day)}")
        await asyncio.sleep(1)


@base_router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.answer('Я тебя не понял.')
    except TypeError:
        await message.answer("Nice try!")
