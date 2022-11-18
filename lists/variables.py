print("Hello World!!!!!!!!!!")

# variables
a=45
print(a)

name="edem kemal"
print(name)

#variable - storage while code runs, varname = value
# note: name should be
#1. should not start with numbers
#2. preferrably start with lower case letter so you know its variable

b=6.87
msg = "Hellom this is Edem"

print(a)
print(b)
print(name)
print(msg)

a = 90

print("a=90")
print(a)

print(a,b,name,msg)
print("I am printing variables", a,b,name,msg)
#PEP8 - python best practices (in coding) guidelines

a = a + 1
print(a)

print('before title', name)
print('name with title', name.title())
print('name after title', name)
print('using is lower:', name.islower())
print('using is upper:', name.isupper())

cars = ['lexus', 'moskvich', 'tesla', 'bmw']
print("Permanent sorting - sort().")
print("List before sorting:", cars)
cars.sort() # by default sorting in ascending order
print("List after sorting:", cars)

names = ['john', 'jane', 'mark']
print("List before sorting:", names)
names.sort(reverse=True)   # sorting in descending order
print("List after reverse sorting", names)

print("Sorting temporarily - sorted()")
car_models = ['corolla', 'camry', 'model x', '550 xi']
print(car_models)
sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True)
print("Car models after sorting:", car_models)
print("sorted car models after sorting in ascending order:", sorted_car_models_asc)
print("sorted car models after sorting in descending order:", sorted_car_models_desc)

print("reversing the list without sorting")
nums = [1,2,3,4,5,6]
print("list before reversing:", nums)
nums.reverse()
print("list after reversing: ", nums)

places = ['hawai', 'paris', 'bahamas', 'iceland']

#loops - executing code rrepetiively (what to loop through how many times
print("looping through entire list: ")

print(f"I want to visit {places[1]} next summer")
#for var_each_element in iterative:
# for var_each_element in list_name:
# print('lines of code to be repeated')
for place in places:
    # comment line
    #print(place)
    print(f"I want to visit {place.title()} next summer")
    print(f"How far is the {place.title()} from new york")

print("ohh, i need to convince my wife now.")
for place in places:
    print(f"How far is the {place.title()} from new york")

#H/W: 4-1, 4-2

print("# Working with list of numbers, range() functions")
#range(5) -> 0,1,2,3,4
#range(2, 6) -> 2,3,4,5
#range(4,16, 3) -> 4,7,10,13 ---last number is n-1
print(range(5))
print( list(range(5)) )

for num in range(0,5,1):
    print(f'Each number : {num}')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for num in range (2,8):
    print(f'Each number: {num}')
print("=======================================================================")
for num in range (2,10,5):
    print(f'Each number: {num}')

print("---------------------------------------------------------")

#problem: list all number between 21 and 36 that can be divided by 4

for num in range (24,37,4):
    print(f'each number divisable by 4 in range 21-36: {num}')

print("-------------------------------------------------------------")
print("#print problem2: list the squares of numbers between 25 and 30")
num_squares = []
for num in range(25,31):
    #print(f'num = {num} and square is: {num**2}')
    num_squares.append(num**2)

print("final list of square numbers:", num_squares)
print("____________________________________")
nums = [4,2,9,10]
print(f'sum of the nums: {sum(nums)}')
sum = 0
for num in nums:
    sum = sum + num
print(sum)

print(1.5+1.4)

edem = [1,2,3,5]
print(edem.insert(4,1000))
print(edem)

edem.insert(2, 2000)
print(edem)

print("=--------------------------------------------------------------")
cubes = []
for num in range(1,11):
    print(num ** 3)
    cubes.append(num**3)
print(f"this is our new list: {cubes}")

print("------------------------------------------------")
#List comprehension

cubes = [num**3 for num in range(1,11)]
print(cubes)

cubes = [num**3 for num in range (1,11)]
print(cubes)

print("-------4-1---------")
pizzas = ['margherita', 'caprisiosa', 'fungi']
for pizza in pizzas:
    print(pizza.title())

print('-------------------------------------')
for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')

print('---------------------------------------')
for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')

print("-----4-2-----------")
animals=['dog', 'cat', 'horse']

for animals in animals:
    print(f' a {animals.title()}- would make a great pet')
print(f'any of these animals would make a great pet')

# chapter 4: slicing the list

