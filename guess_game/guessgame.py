import random

def guess(x):
    random_num =random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess=int(input(f'Guess a number betwwen 1 and {x}:'))
        if guess < random_num:
            print("sorry,Guess agian,Too low")
        elif guess > random_num:
            print("sorry,Guessagain,TOO high")
    print(f"yay!,congrats ,you have guessed the number {random_num} correctly")
def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback != "c":
        if low != high:
            guess= random.randint(low,high)
        else:
            guess=low
        feedback= input(f"Is {guess} too high [H],too low [L] or correct [c]:::").lower()
    
        if feedback == "h" :
            high = guess-1
        elif feedback == "l":
            low = guess+1
    print(f'yey! I have Guessed your number {guess},correctly')

print("Hey there,Lets play a Guess game")
print(f"First Let me take a number .")
print("")
a =int(input("give me number greater than 50: "))
print("I have taken a number between them .Now Guess ")
guess(a)
print("Now it's time to you to take a number and let me Guess")
computer_guess(1000)