from sqlalchemy import create_engine, URL, MetaData
from config import config  # config obyektini import qilamiz

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=config.DB_USER,
    password=config.DB_PASS,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME,
)

engine = create_engine(DATABASE_URL)
metadata_obj = MetaData()
