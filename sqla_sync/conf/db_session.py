import sqlalchemy as sa
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from ..models import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine | None:
    """Create a engine and database: sqlite or postgres"""
    global __engine

    if __engine:
        return

    if sqlite:
        file_db: str = "database/items.db"
        folder: Path = Path(file_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        conn_str: str = f"sqlite:///{file_db}"
        __engine = sa.create_engine(url=conn_str,
                                    echo=False,
                                    connect_args={"check_same_thread": False})
    else:
        conn_str: str = "postgresql://postgres:postpw@localhost:5432/items"  # hardcoded settings xD
        __engine = sa.create_engine(url=conn_str, echo=False)
    return __engine
