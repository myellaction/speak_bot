from aiogram import Bot, Dispatcher
from data import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database



storage = MemoryStorage()
bot = Bot(token=TOKEN_API, parse_mode ='HTML')
dp = Dispatcher(bot=bot, storage=storage)
db = Database()
