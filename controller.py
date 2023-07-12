import view , model

def start():
    while True:
        # view.welcome()
        view.menu()
        answer = input('Выберете команду, набрав соответствующую цифру ')
        if answer == '1':
            date = model.get_data()
            view.show_contacts(date)
        elif answer == '2':
            title = input('Напишите заметку (Заголовок капсом и текст заметки) ')
            # res = model.add_contact(title)
            res = model.add_contact(title)
            view.success(res)

        elif answer == '3':
            contact = input('Введите параметры поиска: ')
            res = model.search(contact)

        elif answer == '4':
            title = input("Введите часть заметки ")
            new = input("Введите изменения ")
            res= model.change(title, new )

        elif answer == "5":
            title = input("Введите часть заметки")
            res = model.delete(title)
        elif answer == "6":
            break
        else:
            view.error()

