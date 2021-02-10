from random import randint
dice_value_freq = [0]*6
for dice_rolled in range(100):
    value_obtained = randint(1,6)
    dice_value_freq[value_obtained-1] += 1

[print(index+1," : ", dice_value_freq[index]) for index in range(6)]

