from aiogram.dispatcher.filters.state import StatesGroup, State

class Speak(StatesGroup):
    send_message = State()