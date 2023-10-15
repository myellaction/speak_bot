from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import InputFile
from gtts import gTTS
import os
from loader import dp
from keyboards.default import get_voice, get_back_menu
from utils.state import Speak
from loader import db


@dp.message_handler(Command('start'), state = '*')
async def cmd_start(message: types.Message):
    await message.delete()
    await db.add_user(message.from_user.id)
    await message.answer(text='Этот бот может озвучивать текст.\n',
                         reply_markup = get_voice())

@dp.message_handler(text = ['📁 Вернуться в меню'], state='*')
async def menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer(text = 'Вы перешли в меню бота.',
                         reply_markup = get_voice())

@dp.message_handler(text='🎵 Озвучить', state = '*')
async def send_voice(message: types.Message):
    await message.delete()
    await Speak.send_message.set()
    await message.answer(text = 'Отправьте сообщение, которое надо озвучить.',
                         reply_markup = get_back_menu())

@dp.message_handler(state=Speak.send_message)
async def make_voice(message: types.Message):
    await message.delete()
    user_id = message.from_user.id
    user = await db.get_user(user_id)
    if not user:
        return await message.answer('Вы не зарегистрированы в боте.\n'
                                             'Для регистрации нажмите <b>/start</b>.')
    lang = (await db.get_language(user_id))[0]
    text = message.text
    name = f'{message.from_user.id}.mp3'
    path = f'tmp_storage/{name}'
    tts = gTTS(text=text, lang=lang)
    tts.save(path)
    await dp.bot.send_voice(chat_id = message.from_user.id,voice = InputFile(path))
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    #path = 'good.mp3'
    #os.remove(path)




