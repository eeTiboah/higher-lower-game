from data import data
from art import logo,vs

import random
print(logo)
score=0
game_data = data
end_game=False
account_list=[]

account_a = random.choice(game_data)
account_b = random.choice(game_data)
if account_a == account_b:
	account_b = random.choice(game_data)
account_list.append(account_a)
account_list.append(account_b)

def mutate_list():
	account_list.pop(0)
	account_c=random.choice(game_data)
	if account_c == account_list[0]:
		account_c=random.choice(game_data)
	account_list.append(account_c)
	end_game=False 


while not end_game:
	print(f"Compare A: {account_list[0]['name']}, a {account_list[0]['description']}, from {account_list[0]['country']} ")
	print(vs)
	print(f"Against B: {account_list[1]['name']}, a {account_list[1]['description']}, from {account_list[1]['country']} ")
	account_a_bool = account_list[0]['follower_count'] > account_list[1]['follower_count']
	account_b_bool = account_list[0]['follower_count'] < account_list[1]['follower_count']
	choice = input("Who has more followers. Type 'A' or 'B': ").lower()
	if choice == 'a' and account_a_bool:
		score+=1
		mutate_list()
		print(f"Correct. Current score is {score} \n")
	elif choice=='b' and account_b_bool:
		score+=1
		mutate_list()
		print(f"Correct. Current score is {score} \n")
	elif (choice=='a' and account_b_bool) or (choice=='b' and account_a_bool):
		print(f"Sorry. That's wrong. Your final score is {score}")
		end_game=True









