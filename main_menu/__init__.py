__all__ = ('router', )

from aiogram import Router

from .base_commands import router as commands_router

router = Router()

router.include_router(commands_router)
