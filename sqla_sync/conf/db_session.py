import sqlalchemy as sa
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models import ModelBase


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


def create_session() -> Session:
    """Create a session with the engine"""
    global __engine

    if not __engine:
        create_engine()
    __session: sessionmaker = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    return __session()


def create_tables() -> None:
    """Create table on database and if is"""
    global __engine

    if not __engine:
        create_engine()
    from models import ModelBase
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
