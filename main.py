import asyncio
import os
import random

from dotenv import load_dotenv
from aiogram import Dispatcher, types, Bot
from os import getenv
from aiogram.filters import Command

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()



@dp.message(Command('pic'))
async def send_pic(message: types.Message):
    # Генератор списка, который создает новый список, включая только те элементы, которые соответствуют условию os.path.isfile, условия в том что он проверяет являются ли они файлами а не подкаталогами.
    files = [f for f in os.listdir('images') if os.path.isfile(os.path.join('images', f))]

    if files:
        # Генерируем случайный индекс с использованием цикла
        random_index = random.randint(0, len(files) - 1)
        while True:
            random_index = random.randint(0, len(files) - 1)
            break

        random_file = os.path.join('images', files[random_index])
        file = types.FSInputFile(random_file)
        await message.answer_photo(
            photo=file,
            caption='Cat'
        )




@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}")

@dp.message(Command('myinfo'))
async def info_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Вас зовут {message.from_user.first_name}, ваш ник {message.from_user.username}, фамилия ваша {message.from_user.last_name}, ваш id {message.from_user.id}")




@dp.message()
async def echo(message: types.Message):
    await message.answer(f"{message.text}, {message.from_user.username}, {message.from_user.full_name}")













async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description='Начало'),
        types.BotCommand(command='pic', description='Рандомное Фото котика'),
        types.BotCommand(command='myinfo', description='Ваше описание')

    ]
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
