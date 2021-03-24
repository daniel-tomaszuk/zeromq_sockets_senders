import asyncio

import uvicorn
from fastapi import FastAPI

from app.main import get_application
from app.monitoring.reporters import stats_reporter
from app.monitoring.reporters import zmq_context

asgi_app: FastAPI = get_application()


@asgi_app.on_event("startup")
async def add_app_db_events_listeners():
    asyncio.create_task(stats_reporter(color="red"))


@asgi_app.on_event("shutdown")
async def add_app_db_events_listeners():
    zmq_context.term()


if __name__ == "__main__":
    # app_workers: int = os.cpu_count() // 6  # https://docs.gunicorn.org/en/stable/design.html#how-many-workers
    app_workers = 1
    uvicorn.run("asgi:asgi_app", host="0.0.0.0", port=8000, timeout_keep_alive=60, workers=app_workers)
