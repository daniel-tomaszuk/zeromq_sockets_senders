import time

from fastapi import APIRouter

from app.api.schemas.common import OKResponse

router = APIRouter()


def init_app(app_instance):
    app_instance.include_router(router, tags=["health"])


@router.get("/health", response_model=OKResponse)
async def health() -> dict:
    return {"status": "ok", "timestamp": int(time.time())}
