# print((-7)/2,"\n",(-7)//2)
# print(2**10,"\n",9**(1/2))
# x = 1234567891011121314
# print(type(x))
# print("""This is a lengthy
#  multiline string containing
# a few lines\
#    of text""")

# x = """This
# is
# a \
    # text"""

# x =10
# print(id(x))
# y = x
# print(id(y))
# x += 5
# print(id(x))
# print(id(y))
x = 10
def update(val):
    print(id(val))
    val = 0
    print(id(val))


print(id(x))
update(x)
print(x)