# Пользовательский интерфейс
import crud
import module_import as import_data
import module_export as export_data

print_employee = lambda data: print(f"\nID= {data.doc_id}"
                                    f"\nПолное имя: \t{data['fullname']}"
                                    f"\nДожлность: \t\t{data['jobPosition']}"
                                    f"\nПодразделение: \t{data['department']}"
                                    f"\nТелефон:\t\t{data['tel']}"
                                    f"\nПочта:\t\t\t{data['email']}")


def ls_menu():
    print('\nHR система')
    while True:
        print('\nМЕНЮ')
        print('1. Поиск сотрудника')
        print('2. Прием на работу')
        print('3. Список сотрудников')
        print('4. Импорт данных по сотрудникам')
        print('5. Эскпорт данных по сотрудникам')
        print('0. Выход\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 0:
            break
        elif n == 1:
            ls_search_employee()
        elif n == 2:
            ls_add_employee()
        elif n == 3:
            ls_all_employees()
        elif n == 4:
            import_data.import_from_csv()
        elif n == 5:
            export_data.export_to_csv()
        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def ls_add_employee():
    crud.add_employee(ls_data_employee())


def ls_all_employees():
    employees = crud.all_employee()

    if len(employees) > 0:
        [print_employee(employee) for employee in employees]
    else:
        print("Нет сотрудников")


def ls_card_employee(data):
    print_employee(data)
    print(f"История сотрудника:")
    [print(a) for a in data["history"]]

    print('\nВыберите действие:')
    print('\t1. Изменить Полное имя')
    print('\t2. Изменить контактные данные')
    print('\t0. Выход')

    change = сhecking_the_number(input('Введите номер пункта: '))
    if change == 0:
        return
    elif change == 1:
        ls_rename_employee(data)
    elif change == 2:
        ls_change_contacts_employee(data)


def ls_rename_employee(data):
    crud.rename_employee(data)


def ls_change_contacts_employee(data):
    crud.contacts_employee(data)


def ls_op_employee(employeeId):
    print('\nВыберите действие:')
    print('\t1. Карточка сотрудника')
    print('\t2. HR операции')
    print('\t0. Выход')

    data = crud.get_by_id(employeeId)

    change = сhecking_the_number(input('Введите номер пункта: '))
    if change == 0:
        return
    elif change == 1:
        ls_card_employee(data)
    elif change == 2:
        ls_hr_employee(data)


def ls_hr_employee(data):
    print('\nВыберите HR операцию')
    print('\t1. Перевод по компаниии')
    print('\t2. Оформление отпуска')
    print('\t3. Оформление больничного')
    print('\t4. Увольнение')
    print('\t5. Повторный прием')
    print('\t0. Выход')

    change = сhecking_the_number(input('Введите номер пункта: '))
    if change == 0:
        return
    elif change == 1:
        crud.transfer_employee(data)
    elif change == 2:
        crud.vacation_employee(data)
    elif change == 3:
        crud.sick_employee(data)
    elif change == 4:
        crud.dismissal_employee(data)
    elif change == 4:
        crud.repeat_employee(data)


def ls_data_employee():
    fullname = input('ФИО сотрудника: ')
    birthDate = input('Дата рождения: ')
    jobPosition = input('Должность сотрудника: ')
    department = input('Отдел: ')
    tel = input('Контактный номер телефона: ')
    email = input('Электронная почта: ')

    return fullname, birthDate, jobPosition, department, tel, email


def ls_search_employee():
    search_str = input(f"Поиск сотрудника: ")

    if not search_str:
        print("Нет данных для поиска")
        return

    result = crud.employee_matching_all(fullname=search_str, birthDate=search_str, jobPosition=search_str,
                                    department=search_str, tel=search_str, email=search_str)

    if not result:
        print("\n!-!-! Сотрудник не найден !-!-!")
        return

    len_search = len(result)
    print(f"Найдено записей: {len_search}")

    [print_employee(cc) for cc in result]

    if len_search > 1:
        select_input = input(f"\nВыберите ID сотрудника: ")
        if not crud.is_int(select_input):
            print(f"Некорректный ввод")
            return

        select_employee = int(select_input)
    else:
        select_employee = result[0].doc_id

    if select_employee:
        ls_op_employee(select_employee)

    # if len_search_data == 0:
    #    continue
    #
    # print(f"Найдено записей: {len_search_data}")
    # [print(f"\nID= {cc.doc_id}"
    #        f"\nПолное имя= {cc['surname']} {cc['name']}"
    #        f"\nТелефон:{cc['number']}"
    #        f"\nЭлектронная почта:{cc['email']}\n")
    #  for cc in search_result]
    #
    # select_contact = 0
    #
    # if len_search_data > 1:
    #     select_input = input(f"\nВыберите ID контакта: ")
    #     if not crud.is_int(select_input):
    #         print(f"Некорректный ввод")
    #         #continue
    #
    #     select_contact = int(select_input)
    # else:
    #     select_contact = search_result[0].doc_id
    #
    # print('1. Изменить контакт.')
    # print('2. Удалить контакт.')
    # print('0. Выход.')
    #
    # change = сhecking_the_number(input('Введите номер пункта: '))
    #
    # if change == 0:
    #     #continue
    # elif change == 1:
    #     change_contact = crud.get_contact_by_id(select_contact)
    #
    #     if len(change_contact) == 0:
    #         print("Не верно указанный ID")
    #         #continue
    #
    #     crud.change_contact(select_contact, get_change_contact(change_contact))
    # elif change == 2:
    #     crud.delete_contact(select_contact)
    # else:
    #     print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.') """


def get_change_contact(change_):
    if len(change_) == 0:
        return
    old_number = ""
    old_email = ""
    name = input(f"Введите имя [{change_['name']}]: ")
    surname = input(f"Введите фамилию [{change_['surname']}]: ")
    change_tel = input(f"Добавить(Y),Изменить(N) номер телефона: ")
    if change_tel == 'N':
        old_number = input(f"Введите номер телефона который нужно изменить: ")
    number = input(f"Введите новый номер телефона: ")

    change_email = input(f"Добавить(Y),Изменить(N) электронную почту: ")
    if change_email == 'N':
        old_email = input(f"Введите электронную почту который нужно изменить: ")
    email = input(f"Введите новую электронную почту: ")

    return name, surname, number, old_number, email, old_email


def get_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = input('Введите номер телефона: ')
    email = input('Введите электронную почту: ')

    return name, surname, number, email


def сhecking_the_number(arg):
    while not arg.isdigit():
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

