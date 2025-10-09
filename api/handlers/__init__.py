from handlers.ping import router as ping_router
from handlers.users import router as users_router
from handlers.tarrif import router as tariff_router

routers = [ping_router, users_router, tariff_router]