from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"Asalomu aleykum siz wikipediya botga xush kelibsiz!!!"
    await message.answer(text)