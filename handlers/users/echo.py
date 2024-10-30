from aiogram import types
import wikipedia

from data.config import ADMINS
from loader import dp

wikipedia.set_lang('uz')


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    text = message.text


    try:
        answer_text=wikipedia.summary(text)
        await message.reply(answer_text)

    except:
        await message.reply("🤷‍♂️Bunday  ma'lumot topilmadi")
