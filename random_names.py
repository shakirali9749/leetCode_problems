"""
1. generate the dataset for firstname
2. generate the dataset for lastname
3. select the random name from firstname and save it in the variable
4. select the random name from lastname and save it in the variable
5. combine the random firstname with random lastname
6. display it to the user
7. take the input from the user whether it be liked or not
8. if liked then break the program
9. if not liked then repeat the process
"""
import random

firstname = ['daniyal', 'ali', 'sufyan', 'waqas', 'amjad', 'adil', 'bilal', 'farhan', 'muneeb','talib', 'uzair', 'hassan', 'shakir', 'hashim']

lastname = ['elahi', 'shah', 'malik', 'khuwaja', 'chaudhar', 'rasheed', 'ahmed', 'makki', 'madni', 'hashmi', 'haji', 'sheikh', 'butt', 'jutt']

while True:
	first_choice = random.choice(firstname)
	last_choice = random.choice(lastname)
	full_name = f'{first_choice} {last_choice}'
	print(f'I created this name: {full_name}')

	user_input = input('Press Y for yes and N for No ?')
	if user_input.lower() == 'y':
		break

input('Press Enter to exit from the program')
