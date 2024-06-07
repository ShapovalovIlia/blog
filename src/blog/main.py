import asyncio
import importlib.resources
from typing import Generator

from fastapi import FastAPI
from uvicorn import Server, Config
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig

import blog.persistence.alembic

async def main() -> None:
    app = FastAPI(title="blog")

    config = Config(app, host="0.0.0.0")
    server = Server(config)

    await server.serve()


ALEMBIC_CONFIG = str(
    importlib.resources.files(
        blog.persistence.alembic,
    ).joinpath("alembic.ini"),
)


def migrate() -> None:
    alembic_config = AlembicConfig(ALEMBIC_CONFIG)
    upgrade(alembic_config, "head")

asyncio.run(main())
