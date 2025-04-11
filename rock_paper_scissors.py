rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_inp = int(input("Welcome to Rock Paper Scissors game. Enter your choice - 0 for Rock, 1 for Paper, 2 for Scissor :"))
comp_inp = random.randint(0,2)
symbols = [rock,paper,scissors]
print(comp_inp)

if user_inp >= 3 or user_inp < 0:
    print("You typed an invalid number. You lose!")
else:
    if user_inp == 0:
        print(f"Your choice is {symbols[user_inp]}")
        if comp_inp == 0:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"Match is a draw!")
        elif comp_inp == 1:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Lose!")
        elif comp_inp == 2:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Win!")
    elif user_inp == 1:
        print(f"Your choice is {symbols[user_inp]}")
        if comp_inp == 0:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Win!")
        elif comp_inp == 1:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"Match is a draw!")
        elif comp_inp == 2:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Lose!")
    elif user_inp == 2:
        print(f"Your choice is {symbols[user_inp]}")
        if comp_inp == 0:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Lose!")
        elif comp_inp == 1:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"You Win!")
        elif comp_inp == 2:
            print(f"Computer choice is {symbols[comp_inp]}")
            print(f"Match is a draw!")