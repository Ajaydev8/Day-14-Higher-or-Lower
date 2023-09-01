import random
from game_data import data

from art import logo,vs

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

def compare():
    is_on = True
    score = 0

    while is_on:

        global account_a
        global account_b

        def get_new_account():
            return random.choice(data)


        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")

        print(vs)

        print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice == 'a' and account_a['follower_count'] > account_b['follower_count']:
            score += 1
            print(f"You're right, Current score: {score}")
            data.remove(account_a)
            account_a = account_b
            account_b = get_new_account()
        elif user_choice == 'b' and account_b['follower_count'] > account_a['follower_count']:
            score += 1
            print(f"You're right, Current score: {score}")
            data.remove(account_a)
            account_a = account_b
            account_b = get_new_account()
        else:
            print(f"Sorry,You're wrong. Your score: {score}")
            is_on = False

game_is_on = True

while game_is_on:
    compare()
    user_choice = input("Do you want to play again? Type 'y' or 'n': ")