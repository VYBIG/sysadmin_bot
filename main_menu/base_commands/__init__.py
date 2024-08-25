__all__ = ('router', )

from aiogram import Router

from .commands import router as commands_router
from .start_and_main_menu import router as start_router

router = Router()

router.include_routers(commands_router,start_router)
