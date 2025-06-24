from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_my_group_schedule():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text='Мое расписание'))
    return builder.as_markup()


def get_days_keyboard():
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Все дни']
    builder = ReplyKeyboardBuilder()
    for day in days:
        builder.add(KeyboardButton(text=day))
    return builder.as_markup()