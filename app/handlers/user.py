import logging

import requests
from aiogram import Router, types, Bot, F
from aiogram import html
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from config import config
from misc.utils import GetFlowerPrediction

user_router = Router()


# сбросить текущее состояние
# этот хендлер должен быть первым!
@user_router.message(Command(commands=["cancel"]))
@user_router.message(F.text.lower() == 'отмена')
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Действие отменено")


@user_router.message(Command("get_prediction"))
async def user_start(message: types.Message, bot: Bot, state: FSMContext):
    photo = FSInputFile('media/iris.png')
    text = '''\
Здравствуйте,
чтобы получить прогноз введите размеры цветка 
(четыре числа разделенные пробелами)zzz'''
    await bot.send_photo(message.chat.id, photo, caption=text)
    await state.set_state(GetFlowerPrediction.data_waiting)


@user_router.message(Command("gp"))
async def cmd_gp(message: types.Message, command: CommandObject, bot: Bot, state: FSMContext):
    # logging.error(command.args)
    if command.args:
        # await message.answer(f"Вы ввели следующие аргументы: {html.code(html.quote(command.args))}")
        photo = FSInputFile('media/iris.png')
        text = '''Щаз будет ответ'''
        await bot.send_photo(message.chat.id, photo, caption=text)
        url = f'{config.api_url}predict_flower'
        a = command.args.split()[:4]
        logging.error(a)
        response = requests.post(url, json={"sepal_length": a[0],
                                            "sepal_width": a[1],
                                            "petal_length": a[2],
                                            "petal_width": a[3]})
        print(iris_predict := response.json()['flower_class'])
        pic = {"Iris Setosa": "media/setosa.png",
               "Iris Versicolour": "media/versicolor.png",
               "Iris Virginica": "media/virginica.png"}
        photo = FSInputFile(pic[iris_predict])
        await bot.send_photo(message.chat.id,
                             photo)  # , caption=iris_predict, reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.answer(f"Пожалуйста, пожалуйста введите аргументы команды {html.code('/gp')}!")


@user_router.message(GetFlowerPrediction.data_waiting)
async def post_get_predict(message: types.Message, bot: Bot, state: FSMContext):
    url = f'{config.api_url}predict_flower'
    a = message.text.split()[:4]
    print(a)
    response = requests.post(url, json={"sepal_length": a[0],
                                        "sepal_width": a[1],
                                        "petal_length": a[2],
                                        "petal_width": a[3]})
    print(iris_predict := response.json()['flower_class'])
    pic = {"Iris Setosa": "media/setosa.png",
           "Iris Versicolour": "media/versicolor.png",
           "Iris Virginica": "media/virginica.png"}
    photo = FSInputFile(pic[iris_predict])
    await bot.send_photo(message.chat.id, photo)  # , caption=iris_predict, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@user_router.message(Command(commands=["help"]))
@user_router.message(F.text.lower() == 'помощь')
async def cmd_cancel(message: Message, state: FSMContext):
    text = '''\
Справка.
Тут будет какая-то помощь для пользователя.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
    await message.answer(text=text)
