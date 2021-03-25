import asyncio
from contextlib import suppress
from datetime import datetime
from datetime import timezone

import psutil
import zmq
import zmq.asyncio
from core.config import settings

zmq_context: zmq.asyncio.Context = zmq.asyncio.Context()


async def stats_reporter():
    process: psutil.Process = psutil.Process()
    sock: zmq.asyncio.Socket = zmq_context.socket(zmq.PUB)
    sock.setsockopt(zmq.LINGER, 1)
    sock.connect("tcp://backend_reporter:8888")

    with suppress(asyncio.CancelledError):
        while True:
            data_to_send = dict(
                timestamp=datetime.now(tz=timezone.utc).isoformat(),
                cpu=process.cpu_percent(),
                mem=process.memory_full_info().rss / 1024 / 1024,
                app_name=settings.APP_NAME,
                color=settings.APP_COLOR,
            )

            await sock.send_json(data_to_send)
            await asyncio.sleep(1)
    sock.close()
