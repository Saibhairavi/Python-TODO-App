
import database

MENU_PROMPT=""" --Coffee BEAN App--
Please select any one option:
1)Add
2)see
3)find by name
4)any best prep

Your choice=
"""

def menu():
    connection=database.connect()
    database.create_tables(connection)
    # user_input=input(MENU_PROMPT)
    while (user_input :=input(MENU_PROMPT))!='5':
        if user_input=='1':
            name,method,rating=input('please enter name,method and rating(between 0-100) resp').split(",")
            database.add_bean(connection, name, method, int(rating))
        elif user_input=='2':
            beans=database.get_all_beans(connection)
            for bean in beans:
                print(bean)
        elif user_input=='3':
            name=input('enter name u want to find')
            bin=database.get_beans_by_name(connection, name)
            print(bin)
        elif user_input=='4':
            name=input('enter name u want to get')
            name=database.get_best_prep_for_bean(connection, name)
            print(name)
        else:
            print('invalid input')


menu()


