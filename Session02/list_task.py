rainbow = ['green', 'orange', 'violet']

violet_index = rainbow.index('violet')

rainbow.insert(violet_index-1,'red')
print(rainbow)

rainbow.append('yellow')
print(rainbow)

rainbow.reverse()
print(rainbow)

rainbow.remove('orange')
print(rainbow)