import random
cpu = ["Rock", "Paper", "Scissors"]
player = input("rock, paper or scissors\n")
r = random.choice(cpu)
print(r)
print(player)
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
if r == cpu[0]:
    print(rock)
elif r == cpu[1]:
    print(paper)
elif r == cpu[2]:
    print(scissors)

play = player.lower()

if play == "rock":
    print(rock)
elif play == "paper":
    print(paper)
elif play == "scissors":
    print(scissors)
else:
    print("Invalid input")


if r == cpu[0] and play == "rock":
    print("Draw")
elif r == cpu[0] and play == "paper":
    print("You win!")
elif r == cpu[0] and play == "scissors":
    print("You lose!")
if r == cpu[1] and play == "rock":
    print("You lose!")
if r == cpu[1] and play == "paper":
    print("Draw!")
if r == cpu[1] and play == "scissors":
    print("You win!")
if r == cpu[2] and play == "rock":
    print("You win!")
if r == cpu[2] and play == "paper":
    print("You lose!")
if r == cpu[2] and play == "scissors":
    print("Draw!")






