import os

from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()

engine = create_engine(
    os.getenv("DB_URL"),
    echo=True,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=-1,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={
        "connect_timeout": 60,
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5,
    },
)