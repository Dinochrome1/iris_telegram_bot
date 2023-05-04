import requests
from aiogram import Router, types, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

from config import config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: types.Message):
    await message.reply("Здравствуй, обычный пользователь!")


@user_router.message(Command("get_predict"))
async def post_get_predict(message: types.Message, bot: Bot):
    url = f'{config.api_url}predict_flower'
    a = message.text.split()[1:5]
    print(a)
    response = requests.post(url,
                             json={"sepal_length": a[0],
                                   "sepal_width": a[1],
                                   "petal_length": a[2],
                                   "petal_width": a[3]})

    # print(iris_predict := response.json())
    print(iris_predict := response.json()['flower_class'])

    pic = {"Iris Setosa": "media/setosa.png",
           "Iris Versicolour": "media/versicolor.png",
           "Iris Virginica": "media/virginica.png"}

    photo = FSInputFile(pic[iris_predict])
    await bot.send_photo(message.chat.id, photo, caption=iris_predict)
