import random

def play():
    user =input("what's your choice \n 'r' for Rock\n 'p' for Paper \n 's' for Stone\n").lower()
    computer = random.choice(['r','p','s'])
    print(f"computer picked {computer}")
    if user == computer:
        return "It's a tie"
    if is_win(user,computer):
        return "You won !!"
    return "You lose...."

def is_win(player,opp):
    if(player == 'r'and opp == 's' ) or (player == 's' and opp =='p') \
        or (player == 'p' and opp =='r'):
        return True

print(play())