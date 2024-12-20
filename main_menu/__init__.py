__all__ = ('router',)

from aiogram import Router

from .base_commands import router as commands_router
from .main_functions import router as main_functions_router

router = Router()

router.include_routers(main_functions_router,commands_router,)
