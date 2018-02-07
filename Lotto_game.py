import random
from sys import exit 
def Lotto():
    #int(input()) for x in range(5)
    #lottery_numbers = [random.randint(1, 20) for x in range(5)]
    lottery_numbers = (random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
    lottery_pot = 100000000
    while True:
        print("Would you like to enter the POWER SUPER MAX MEGGA MILLIONARE MONEY LOTTERY!!?")
        print("1. Yes")
        print("2. No")

        reply = input("> ")

        if reply == 'yes' or reply == 'Yes':
            guesses = get_five()

        if reply == 'no' or reply == 'No':
            print("See ya later!")
            exit() 
    
        if guesses == lottery_numbers:
            print("Congradulations you win the lottery!!!!")
            print(lottery_numbers)
            print(lottery_pot)

        else:
            print("So sad too bad you did not win th lottery this time.")
            print(lottery_numbers)
            print("10 million will be added to the pot.")
            lottery_pot += 10000000
            print("The lottery total is now",lottery_pot)

def get_five():
    guesses = []
    
    while len(guesses) < 5:
        try:
            int_val = int(input("Enter in a interger value from 1 to 20: "))
            if int_val > 20:
                print("That value is not exceptable...")
            elif int_val in guesses:
                print("This number has already been entered...")
            else:
                guesses.append(int_val)
        except ValueError:
            print("Please enter a whole number value. ")
    

    return guesses

Lotto()