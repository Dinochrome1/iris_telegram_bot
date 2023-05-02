import requests
from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from config import config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: types.Message):
    await message.reply("Здравствуй, обычный пользователь!")


@user_router.message(Command("ping"))
async def get_ping_pong(message: types.Message):
    url = config.api_url
    response = requests.get(url)
    await message.reply(str(response.json()))


@user_router.message(Command("t"))
async def post_get_predict(message: types.Message):
    url = f'{config.api_url}predict_flower'
    a = message.text.split()[1:5]
    response = requests.post(url,
                             json={"sepal_length": a[0],
                                   "sepal_width": a[1],
                                   "petal_length": a[2],
                                   "petal_width": a[3]})
    await message.reply(str(response.json()))
