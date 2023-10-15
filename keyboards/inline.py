from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from utils.const import languages
from aiogram.utils.callback_data import CallbackData

cb_languages = CallbackData('change_lang','kind')

def get_language():
    markup = InlineKeyboardMarkup(row_width=3)
    for i in languages:
        markup.add(InlineKeyboardButton(text=languages[i], callback_data=cb_languages.new(kind=i)))
    return markup


