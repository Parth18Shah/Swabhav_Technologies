# part 1 
names = ['MUMBAI', 'PUNE', 'AHMEDABAD']
lower_names = [i.islower() for i in names]
print(lower_names)

nos = [10, 20, 30, 40]

double_nos = [i*i for i in nos]
print(double_nos)

# part 2 
mylist = [10,20,30,40]
new_list = [ i for i in mylist if i>20]
print(new_list)

new_list = [ i if i>20 else 0 for i in mylist]
print(new_list)


# part 3
from random import randint
random_list = [ randint(1,5) for i in range(10) ]

number_list = [[1,2,3], [4,5,6], [7,8,9]]
new_list = [value for sublist in number_list for value in sublist]
print(new_list)