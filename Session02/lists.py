# print("Hello world")

item1 = [10,20,30,'swabhav']
item2 = item1
print("Id for item1",id(item1))
print("Id for item2",id(item2))
item2[3] = 'techlabs'
print(item1)
print("Id for item1",id(item1))
print("Id for item2",id(item2))