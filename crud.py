# Операции обработки данных
# Создание, Чтение, Изменение, Удаление

import functools
from tinydb import TinyDB, Query
from datetime import datetime

from tinydb.queries import QueryLike

global db

db = TinyDB('db.json', ensure_ascii=False, encoding='utf-8')
employees = db.table("Employees")
department = db.table("Department")

query = Query()


def init_db():
    db.table("Employees")
    db.table("Department")

def import_employee(data):
    if not data:
        return

    if employees.contains(query.fullname == data[0]):
        return f"!! Сотрудник с похожит ФИО уже существует !!"


    employee = {
        "fullname": data[0],
        "birthDate": data[1],
        "jobPosition": data[2],
        "department": data[3],
        "tel": data[4],
        "email": data[5],
        "status": data[6],
        "history": [f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} Импорт из файла {list(data)}"]
    }

    return f"Запись успешно добавлена, ID:{employees.insert(employee)}"


def add_employee(data):
    employee = {
        "fullname": data[0],
        "birthDate": data[1],
        "jobPosition": data[2],
        "department": data[3],
        "tel": data[4],
        "email": data[5],
        "status": "Работает",
        "history": [f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} "
                    f"Принят на работу в отдел {data[3]} на позицию {data[2]}"]
    }
    if employees.contains(query.fullname == data[0]):
        return f"!! Сотрудник с похожит ФИО уже существует !!"

    employees.insert(employee)


test_contains = lambda value, search: search in value


def employee_matching_all(**query):
    q = Query()
    return employees.search(functools.reduce(lambda x, y: x | y,
                                             [getattr(q, k).test(test_contains, str(v))
                                              for k, v in query.items()]))


def all_employee():
    return employees.all()


def transfer_employee(data):
    if not data:
        return

    toDept = input("Укажите новый отдел: ")
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Перевод из отдела {data['department']}  на позицию {toDept}")

    result = employees.update({"department": toDept, "history": history}, doc_ids=[data.doc_id])

    if result:
        print("Перевод по компании успешно проведен")


def vacation_employee(data):
    if not data:
        return
    vacationDate = input("Укажите дату окончания отпуска: ")
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Плановый отпуск с {datetime.today().strftime('%Y-%m-%d')} по {vacationDate}")

    result = employees.update({"status": "В отпуске", "history": history}, doc_ids=[data.doc_id])

    if result:
        print("Отпуск успешно проведен")


def sick_employee(data):
    if not data:
        return

    sickDate = input("Укажите дату окончания  больничного: ")
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Больничный с {datetime.today().strftime('%Y-%m-%d')} по {sickDate}")

    result = employees.update({"status": "На больничном", "history": history}, doc_ids=[data.doc_id])
    if result:
        print("Больничный успешно проведен")


def dismissal_employee(data):
    if not data:
        return
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Уволен {datetime.today().strftime('%Y-%m-%d')}")

    result = employees.update({"status": "Уволен", "history": history}, doc_ids=[data.doc_id])
    if result:
        print("Увольнение успешно проведено")


def repeat_employee(data):
    if not data:
        return
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Принят на работу {datetime.today().strftime('%Y-%m-%d')}")

    result = employees.update({"status": "Работает", "history": history}, doc_ids=[data.doc_id])
    if result:
        print("Прием на работу успешно проведено")


def rename_employee(data):
    if not data:
        return

    rename = input("Укажите полное имя: ")
    history = data["history"]
    history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                   f"Переименование с {data['fullname']} на  {rename}")

    result = employees.update({"fullname": rename, "history": history}, doc_ids=[data.doc_id])

    if result:
        print("Переименование сотрудника успешно выполнено")


def ls_change_contacts_employee(data):
    if not data:
        return
    print("Чтобы удалить контакт, укажите значение del")
    tel = input(f"Изменить контактный телефон с {data['tel']} на: ")
    email = input(f"Изменить электронную почту с {data['email']} на: ")

    if tel == "del":
        tel = ""
    elif tel == "":
        tel = data["tel"]

    if email == "del":
        email = ""
    elif tel == "":
        email = data["email"]

    history = data["history"]

    if tel != data["tel"]:
        history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                       f"Изменение контактного телефона с {data['tel']} на {tel}")
    if email != data["email"]:
        history.append(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                       f"Изменение электронной почты с {data['email']} на {email}")

    result = employees.update({"tel": tel, "email": email, "history": history}, doc_ids=[data.doc_id])

    if result:
        print("Изменение контактных данных сотрудника успешно завершено")


def get_by_id(id):
    return employees.get(doc_id=id)
