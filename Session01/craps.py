from random import randint

def getsum():
    # to get the sum of values obtained on rolling the dice twice
    return randint(1,6) + randint(1,6)

def game():
    # contains the logic behind this game
    while isGameOver==False:
        first_roll_sum = getsum()
        print("The sum obtained on rolling the dice is:",first_roll_sum)
        if(first_roll_sum in (7, 11)):
            return 1
        elif(first_roll_sum in (2, 3, 12)):
            return 0
        elif(first_roll_sum in (4, 5, 6, 8, 9, 10)):
            point_obtained = first_roll_sum
            nextRoll = True
        
        while nextRoll:
            new_roll_sum = getsum()
            print("The sum obtained on rerolling the dice is:",new_roll_sum)
            if(new_roll_sum == first_roll_sum):
                return 1

            if(new_roll_sum == 7):
                return 0

point_obtained = 0
isGameOver = False
nextRoll = False
print("--------------Welcome to A Game of Chance--------------")
while True:
    game_Result = game()
    if(game_Result):
        print("You win.")
    else:
        print("You lose.")
    
    choice = input("Would you like to play again? (y/n): ")
    if(choice=='n'):
        print("--------Thank You for playing A Game of Chance--------")
        break
