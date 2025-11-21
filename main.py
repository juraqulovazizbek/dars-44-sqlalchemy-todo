from database import engine, metadata_obj
from crud import create_task, get_tasks, update_task, delete_task, change_task_status

# Jadvallarni yaratish
metadata_obj.create_all(engine)

# CREATE test
create_task("Uy ishini tugatish (database)", "darsni to'liq ko'rib chiqish, sinab ko'rish")
create_task("Dars qilish", "Python loyihasi")

# READ test
print("TASKLAR:")
for t in get_tasks():
    print(f"{t.id} | {t.title} | {t.description} | {t.completed}")

# UPDATE test
update_task(1, title="darsni tugatish (database)", description="darsni qilish kkda eee")

# STATUS toggle test
change_task_status(1)

# DELETE test
delete_task(1)

# FINAL RESULT
print("\nFINAL TASKLAR:")
for t in get_tasks():
    print(f"{t.id} | {t.title} | {t.description} | {t.completed}")
