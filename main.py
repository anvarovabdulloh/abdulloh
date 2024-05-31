
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from logging import basicConfig, getLogger, INFO


basicConfig(level=INFO)
log = getLogger()

storage = MemoryStorage()

BOT_TOKEN = "6332602698:AAGl97iZvXnq0lHZg7QUEMrB54Mgie2wf4c"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer("Salom yangi bot")


if __name__ == '__main__':
    executor.start_polling(dp)
