# part 1
t1 = (10, 20)
print(id(t1))
t1 += (3,4)
print(id(t1))
print(t1,"A new tuple had been created on adding a new element.")


# part 2
l1 = [10,20]
print("\nId before adding:",id(l1))
l1+=(30,40)
l1+="hello"
print("Id after adding:",id(l1))
print(l1,"\nThe values will be added to the same list.\n")


# part 3
student_tuple = ('Lesha', [10,20,30])
print(student_tuple[1][0])
print("Id before changing a value:",id(student_tuple))
student_tuple[1][0] = 100
print(student_tuple[1][0])
print("Id after changing a value:",id(student_tuple))