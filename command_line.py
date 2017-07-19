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

	name = input('Enter Name:\n> ')
	weight = input('Enter your current weight:\n> ')

	create_user(name, weight)

def choose_active_user_cli():

	'''ensure we have no active users'''
	deactivate_active_user()

	print('Who are you?\n')

	users = list_users()
		
	for user_id, name in users:
		print(user_id, name)

	try:
		user_input = int(input('> '))

		if user_input == 0:
			print('You must select an active user.')
			choose_active_user_cli()

		elif user_input <= len(users):

			activate_user(user_input)
			print('Active User is {}'.format(active_user))

		elif user_input > len(users):
			print('You must select an active user.')
			choose_active_user_cli()

	except ValueError:
		print('You must select an active user.')

def weigh_in_cli():
	global active_user

	if active_user:
		weight = input('Enter your current weight:\n> ')

		weigh_in(active_user, weight)

	else:
		print('You must select an active user.')
		choose_active_user_cli()

def weight_history_cli():
	global active_user

	try:
		weight_history = user_weight_history(active_user)

		if weight_history is not None:
			for date, weight in weight_history:
				print('On ' + str(date) + ' Your Weight: ' + str(weight))
			input('-> press return go back to the main menu')
		else:
			print('Active User has no weight history\n')
			input('-> press return go back to the main menu')

	except sqlite3.OperationalError:
		print('You must select an active user.')
		choose_active_user_cli()




