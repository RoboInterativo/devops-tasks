from aiogram.fsm.state import StatesGroup, State


class DayState(StatesGroup):
    day = State()


class ReportState(StatesGroup):
    report_message = State()
