from aiogram import Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import BotCommand, BotCommandScopeDefault

from config import config


async def set_commands(bot: Bot):
    commands = [  # BotCommand(command='start', description='Начало работы'),
        BotCommand(command='get_prediction', description='получить прогноз'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='cancel', description='Сбросить')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_startup(bot: Bot, admin: int = config.admin_id):
    await set_commands(bot)
    await bot.send_message(admin, "Бот запущен", disable_notification=True)


async def on_stop(bot: Bot, admin: int = config.admin_id):
    await bot.send_message(admin, "Бот остановлен", disable_notification=True)


class GetFlowerPrediction(StatesGroup):
    data_waiting = State()
