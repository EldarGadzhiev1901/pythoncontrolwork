def menu():
    print(
        '1 - Отобразить все заметки \n'
        '2 - Добавить заметку \n'
        '3 - Найти заметку \n'
        '4 - Изменить заметку \n'
        '5 - Удалить заметку \n'
        "6 - Выход \n"
    )
def error():
    return None

def show_contacts(date):
    path = 'file.md'
    data = open(path, 'r')
    print(data.readlines())
    data.close()



def success(date):
    print ("Сохранено ")

def fail(date):
    print ("Ошибка ")

    

if __name__ == '__main__':
    menu()


