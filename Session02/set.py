# s1 = set([10,20])
# s1.add([30,40])
# s1.add([50,60])
# s1.add("hello")

input_string = 'to be or not to be that is the question'
string_set = list(set(input_string.split()))
string_set.sort()
print(string_set)