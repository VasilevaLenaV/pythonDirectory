# Импорт данных в телефонный справочник
import crud as crud

def import_from_csv():
    file = open("import.csv",  mode='r', encoding='utf-8-sig')
    for str_row in file:
        data_to_import = str_row.replace("\n", "").split(";")

        if data_to_import:
            if data_to_import[0] == "fullname":
                continue
            else:
                print(f"Результат: {crud.import_employee(data_to_import)}")

    file.close()

    print(f"Импорт завершен")
