## CHAPTER 6: LOOPING THROUGH A DICTIONARY:

#Dictionaries keys, only values, key and value

person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny'}

#default case
for i in person1.keys():
    print(i)

print("#looping through keys only")
for i in person1:
    print(i)

print("#looking throigh values only")
for value in person1.values():
    print(value)

print("#looping values if we know keys")
for key in person1.keys():
    print('key in this iteration is: ', person1['name'])
    print('key in this iteration is: ', key)
    print('key in this iteration is: ', person1[key])

print("========================================================")
print("#looping through values only -------------------")
for value in person1.values():
    print('value in this iteration is ', value)

print("#looping through keys and values----------------")
for key, value in person1.items():
    print('key in this iteration: ', key)
    print('value in this iteration is: ', value)


#Exercises 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through.One key-value pair might be 'nile':'egypt',
#USE a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

print("                                                                              ")

rivers_countries = {'nile': 'egypt',
                    'amazon': 'brazil',
                    'volga': 'russia',
                    'mississippi': 'usa',
                    'thames': 'uk'}

for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}")

print("                                       ")
for river in rivers_countries.keys():
    print(f"{river.title()} is one of the rivers in the dictionary")

print(" ")
for country in rivers_countries.values():
    print(f"{country.title()} is one of the countries in the dictionary")

b = {'num1':45, 'num2':55, 'num3': 22, 'num4': 55}
print(b['num1'])
