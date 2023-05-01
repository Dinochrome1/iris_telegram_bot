from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import config


class AdminFilter(BaseFilter):
    async def __call__(self, obj: Message) -> bool:
        return obj.from_user.id == config.admin_id
    