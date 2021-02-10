# < - left align > - right align

# task 1
# def add(a,b):
#     print(f'{a:,.2f} + {b:,.2f} = {a+b:>15,.2f}')

# def foo(a,b):
#     print(a,b)

# shares = (10000.567,10000.567)
# # add(shares)

# add(*shares)

# add(*[10000.567,10000.567])

# foo(*'Hi')


# task 2

def calculate_product(*argv):
    product = 1
    for argument in argv:
        product *= argument 
    return product

print(calculate_product(10,20,30))
print(calculate_product(*[i for i in range(1,6,2)]))