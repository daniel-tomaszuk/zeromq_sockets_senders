import os

import uvicorn
from fastapi import FastAPI

from app.main import get_application

asgi_app: FastAPI = get_application()

if __name__ == "__main__":
    app_workers: int = os.cpu_count() // 6  # https://docs.gunicorn.org/en/stable/design.html#how-many-workers
    uvicorn.run("asgi:asgi_app", host="0.0.0.0", port=8000, timeout_keep_alive=60, workers=app_workers)
