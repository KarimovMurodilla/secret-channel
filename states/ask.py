from aiogram.dispatcher.filters.state import State, StatesGroup


class Ask(StatesGroup):
	step1 = State()