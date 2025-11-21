from sqlalchemy import (
    insert, select, update, delete
)
from database import engine
from tables import tasks_table


def create_task(title: str, description: str | None = None):
    with engine.connect() as connection:
        stmt = insert(tasks_table).values(title=title, description=description)
        connection.execute(stmt)
        connection.commit()

def get_tasks():
    with engine.connect() as connection:
        stmt = select(tasks_table)
        return list(connection.execute(stmt))

def update_task(pk: int, title: str | None = None, description: str | None = None):
    with engine.connect() as connection:
        stmt = update(tasks_table).where(tasks_table.columns.id == pk).values(title=title, description=description)
        connection.execute(stmt)
        connection.commit() 

def delete_task(pk: int):
      with engine.connect() as connection:
        stmt = delete(tasks_table).where(tasks_table.columns.id == pk)
        connection.execute(stmt)
        connection.commit() 

def change_task_status(pk: int):
    with engine.connect() as connection:
        stmt = update(tasks_table).where(tasks_table.columns.id == pk).values(completed=True)
        connection.execute(stmt)
        connection.commit() 

# # a = get_user_by_username("rgerg")
# # print(a)
    
# delete_user("vali")
