from aiogram import Router, types
from aiogram.filters import CommandStart, Command
# from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: types.Message):
    await message.reply("Здравствуй, обычный пользователь!")


@user_router.message(Command("ping"))
async def cmd_answer(message: types.Message):
    await message.answer("pong")
