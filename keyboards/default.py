from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def get_voice():
    return ReplyKeyboardMarkup(keyboard = [
        [KeyboardButton('🎵 Озвучить'),KeyboardButton('🗣 Изменить язык') ]
    ], resize_keyboard=True)

def get_back_menu():
    return ReplyKeyboardMarkup(keyboard = [
        [KeyboardButton('📁 Вернуться в меню')]
    ], resize_keyboard=True)

