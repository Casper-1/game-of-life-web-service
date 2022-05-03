import uvicorn

from src.settings import settings

uvicorn.run(
    'life.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
