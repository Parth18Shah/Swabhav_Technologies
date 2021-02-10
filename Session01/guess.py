from random import randint

play = True
while(play):
    value = randint(1,10)
    count = 0
    flag = True
    while(flag):
        userinput = int(input("Your guess: "))
        count += 1
        if(userinput>value):
            print("Too high.")
        elif(userinput==value):
            print("You guessed it in",count,"tries.")
            flag = False
        else:
            print("Too low.")
    choice = input("Would you like to play again? (y/n): ")
    if(choice=='n'):
        play = False

print("Bye!")