# Экспорт данных из телефонного справочника
import crud
import csv


def export_to_csv():
    data = crud.all_employee()
    import csv

    header = ['fullname', 'birthDate', 'jobPosition', 'department', 'tel', 'email', 'status']

    with open('export.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)

        for x in data:
            writer.writerow([x['fullname'], x['birthDate'],x['jobPosition'],x['department'],x['tel'],x['email'],x['status']])

    #     with open('export.csv', 'w', newline='', encoding='utf-8') as f:
    #         for x in data:
    #             writer = csv.writer(f, delimiter=';')
    #
    # #            writer = csv.writer(f, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #             writer.writerow([x['fullname'], x['jobPosition'],str.join(",", x['department']),str.join(",",x['tel']),str.join(",",x['email']).replace("\n","")])
    #

    print(f"Экспорт завершен")
