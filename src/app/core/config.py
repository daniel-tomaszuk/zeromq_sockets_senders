import os
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List


def get_default_allowed_hosts() -> List[str]:
    return os.environ.get("ALLOWED_HOSTS") or ["*"]


@dataclass
class AppSettings:

    DEBUG: bool = True
    PROJECT_NAME: str = "ZeroMQ-Sockets-Sender"
    ALLOWED_HOSTS: List[str] = field(default_factory=get_default_allowed_hosts)

    @staticmethod
    def _prepare_debug(val: Any) -> bool:
        return str(val).lower() in ("true", "1")


settings = AppSettings()
PROJECT_NAME = settings.PROJECT_NAME
DEBUG = settings.DEBUG
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
