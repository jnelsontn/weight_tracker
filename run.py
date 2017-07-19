'''handles the actual cli display'''
from command_line import *

def build_menu():
    print('1. Create User')
    print('2. Choose Active User')
    print('3. Weigh In')
    print('4. User Weight History')
    print('5. Quit')

def check_db():
    check_for_database()
    start_program_menu()

def start_program_menu():
    build_menu()

    choice = input('> ')

    if choice == '1':
        create_user_cli()

    if choice == '2':
        choose_active_user_cli()

    if choice == '3':
        weigh_in_cli()

    if choice == '4':
        weight_history_cli()

    if choice == '5':
        quit()

    start_program_menu()

if __name__ == '__main__':
    check_db()


