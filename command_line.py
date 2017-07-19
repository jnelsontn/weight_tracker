from functions import *

active_user = None

def activate_user(user_id):
    global active_user
    active_user = user_id

    return active_user

def deactivate_active_user():
    global active_user
    active_user = None

    return active_user

def create_user_cli():

    name = input('Enter name:\n> ')
    weight = input('Enter current weight:\n> ')

    if len(name) < 3 or len(weight) <= 2:
        print('Enter a valid name and weight.')
        create_user_cli()
    else:
        create_user(name, weight)

def choose_active_user_cli():
    '''ensure we have no active users'''
    deactivate_active_user()

    users = list_users()

    if len(users) <= 0:
        print('No Users. Create a user.')
        return

    print('Choose active user.\n')

    i = 1
    for index in range(len(users)):
        print(str(i) + '. ' + str(users[index][1]))
        i += 1

    try:
        user_input = int(input('> '))
        user_input = user_input - 1
        activate_user(users[user_input][0])

    except:
        print('Select a user.')
        choose_active_user_cli()

def weigh_in_cli():
    global active_user

    if active_user:
        weight = input('Enter current weight:\n> ')

        weigh_in(active_user, weight)

        try:
            results = compare_previous_and_current_weigh_in(active_user)
            print('initial: {}, previous: {}, current: {}.'.format(
                results[0], results[1], results[2]))
        except:
            pass

    else:
        print('Select a user.')
        choose_active_user_cli()
        weigh_in_cli()

def weight_history_cli():
    global active_user

    try:
        weight_history = user_weight_history(active_user)

        if weight_history is not None:
            for date, weight in weight_history:
                print('date: ' + str(date) + ' weight: ' + str(weight))
            input('-> press return to go back to the main menu')
        else:
            print('User has no history\n')
            input('-> press return to go back to the main menu')

    except sqlite3.OperationalError:
        print('Select a user.')
        choose_active_user_cli()
        weight_history_cli()




