import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config
from handlers.admin import admin_router
from handlers.echo import echo_router
from handlers.user import user_router
from misc.utils import on_startup, on_stop

logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)


async def main():
    logger.info("Starting bot")
    storage = MemoryStorage()
    bot = Bot(token=config.bot_token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    for router in [admin_router, user_router, echo_router]:
        dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_stop)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот был выключен!")
