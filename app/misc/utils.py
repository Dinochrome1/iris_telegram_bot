from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


from config import config


async def set_commands(bot: Bot):
    commands = [BotCommand(command='start',
                           description='Начало работы'),
                BotCommand(command='help',
                           description='Помощь'),
                BotCommand(command='ping',
                           description='если хочешь получить понг?'),
                BotCommand(command='get_predict',
                           description='получить предсказание'),
                BotCommand(command='cancel',
                           description='Сбросить')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def on_startup(bot: Bot, admin: int = config.admin_id):
    await set_commands(bot)
    await bot.send_message(admin, "Бот запущен", disable_notification=True)


async def on_stop(bot: Bot, admin: int = config.admin_id):
    await bot.send_message(admin, "Бот остановлен", disable_notification=True)


