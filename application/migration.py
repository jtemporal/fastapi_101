import databases
import sqlalchemy


DATABASE_URL = "sqlite:///./test.db"

DATABASE = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

QUOTES = sqlalchemy.Table(
    "quotes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)