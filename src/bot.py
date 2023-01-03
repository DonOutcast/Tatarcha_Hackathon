import asyncio
import logging

import aiogram.filters
from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
from aiogram.filters import Command
from aiogram import flags
from aiogram import BaseMiddleware

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=API_TOKEN, parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@flags.chat_action
@dp.message(aiogram.filters.Text(contains="start", ignore_case=True, ), flags={'typing': True})
async def cmd_start(message: types.Message):
    await asyncio.sleep(15)
    await message.answer("<b>Hello!</b>")
    a = await bot.send_dice(message.from_user.id)
    print(a.dice)


async def cmd_test(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, text="Hello World")


dp.message.register(cmd_test, Command("test"))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
