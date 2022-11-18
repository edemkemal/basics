cars= ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw' or 2==2 and ('hello' == 'HELLO'):
        print(f'car value was bmw so we are doing print differently: {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title(): {car.title()}')

print("===========================================================")

# Expressions:

name = 'john'
num = 45.55
is_good = True
friends = []

#Expressions return True/False
name == 'jane'  # False, this is checking if name value variable is equal to Jane
name > 'abc' # A-Z(a,b,....j
num == 45 # FALSE
num > 45 # TRUE
num < 45 # FALSE
num <= 45 # FALSE
num >= 45 # FALSE
num > 45 # TRUE
is_good == False # FALSE
name != 'jane'
#Multiple conditions
name == 'john' and num > 45 # TRUE + TRUE = TRUE
name == 'john' and num < 45 # TRUE + FALSE = FALSE

name == 'john' or num > 45 # True or TRUE = TRUE
name == 'john' or num < 45 # True or False >> True
name == 'jane' or num < 45 # False or False >> False

if friends:
    print('this is not empty list')
else:
    print('friends expression returned false, this mean it is a empty list')
print("===========================================================")
#cars = ['audi', 'bmw', 'subaru', 'toyota']
print(cars)

if 'tesla' in cars:
    print(f'Cars list includes tesla ')
else:
    print(f'tesla is not in the cars list.')


#Exercise 5-1:
print("========================EXERCSE 5-1=============================")



