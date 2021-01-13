import random
while True:
    CHANCES = 3
    number = random.randint(1,10)
    print("Guess a number between 1 and 10.")
    for i in range(CHANCES):
        print("You have {} chances.".format(CHANCES-i)) if((CHANCES-i)>1) else print("You have {} chance.".format(CHANCES-i))

        guess = int(input("Your guess: "))
        if(guess == number):
            print("Congratz! You won! The number was {}.".format(number))
            break
        elif(guess < number):
            print("Nope... A little higher!") if((CHANCES-i)>1) else print("You lost! The number was {}.".format(number))
        elif(guess > number):
            print("Nope... A little lower!") if((CHANCES-i)>1) else print("You lost! The number was {}.".format(number))

    opt = input("Press (1) to play again or (0) to exit the program.")
    if(opt == '0'):
        print("Exiting...")
        exit(0)