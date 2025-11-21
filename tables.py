from sqlalchemy import Table, Column, Integer, String, Boolean
from database import metadata_obj

tasks_table = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('description', String(255), nullable=True),
    Column('completed', Boolean, default=False)
)
