from loader import dp, db
from aiogram import types
from keyboards.inline import get_language, cb_languages
from utils.const import languages


@dp.message_handler(text='🗣 Изменить язык')
async def change_language(message: types.Message):
    await message.delete()
    await message.answer(text='Выберите язык озвучки',
                         reply_markup = get_language())

@dp.callback_query_handler(cb_languages.filter())
async def make_choice(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer()
    user_id = callback.from_user.id
    user = await db.get_user(user_id)
    language = callback_data.get('kind')
    if not user:
        return await callback.message.answer('Вы не зарегистрированы в боте.\n'
                                       'Для регистрации нажмите <b>/start</b>.')
    await db.change_language(user_id, kind=language)
    await callback.message.answer(text=f'Вы выбрали язык озвучки: {languages[language]}')
