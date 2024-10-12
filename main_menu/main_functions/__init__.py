__all__ = ('router',)

from aiogram import Router

from .bit_to_byte_func import router as bit_to_byte_router
from .ip_calc_func import router as ip_calc_router
from .ip_info_func import router as ip_info_router
from .mac_vendor_func import router as mac_vendor_router
from .nslookup_func import router as nslookup_router
from .password_gen_func import router as password_gen_router
from .phone_number_func import router as phone_number_router
from .ping_func import router as ping_router
from .ports_check_func import router as ports_check_router
from .qr_code_maker_func import router as qr_code_maker_router
from .tracert_func import router as tracert_router
from .useful_command_func import router as useful_command_router
from .mac_converter_func import router as mac_converter_router
from .file_converter import router as file_converter_router
router = Router()

router.include_routers(bit_to_byte_router,
                       ip_calc_router,
                       ip_info_router,
                       mac_vendor_router,
                       nslookup_router,
                       password_gen_router,
                       phone_number_router,
                       ping_router,
                       ports_check_router,
                       qr_code_maker_router,
                       tracert_router,
                       useful_command_router,
                       mac_converter_router,
                       file_converter_router,
                       )
