'''calls the functions defined in functions.py'''
from functions import Functions

class Command_Line:
	'''remember we need to activate and deactivate users'''

	def create_user_cli(self):

		name = input('Enter Name:\n> ')
		weight = input('Enter your current weight:\n> ')

		Functions.create_user(self, name, weight)

	def list_users_cli(self):
		print('Who are you?\n')

		users = Functions.list_users(self)
		print(users)


if __name__ == '__main__':
    app = Functions()
    command_line = Command_Line()
    command_line.list_users_cli()
    #command_line.create_user_cli()


    # app.create_user('Aldona', '209')
    # app.weigh_in(1, 208)
    #x = app.user_weight_history(1)
    # x = app.compare_previous_and_current_weigh_in(2)