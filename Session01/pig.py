from random import randint

def getdicevalue():
    # to get the value obtained on rolling the dice
    return randint(1,6) 

turns_taken = 1
total_score = 0
turn_score = 0

print("TURN 1")

while total_score<20:
    option_taken = input("Roll or hold? (r/h):")

    if(option_taken=='r'):
        value_obtained = getdicevalue()
        print("Die: ",value_obtained)
        if(value_obtained==1):
            turn_score = 0
            turns_taken += 1
            print("Turn over. No score.\n\nTURN",turns_taken)
        else:
            turn_score += value_obtained
    
    else:
        total_score += turn_score
        if(turn_score>20 or total_score>20):
            break
        print("Score for turn:",turn_score,"\nTotal score:",total_score)
        turns_taken += 1
        print("\nTURN",turns_taken)
        turn_score = 0
    
    if(turn_score>20 or total_score>20):
        break


print("You finished in",turns_taken,"turn/s!\nGame Over!")


