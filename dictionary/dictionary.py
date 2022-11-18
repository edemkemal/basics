##chapter 6 - Dictionary -data structure(key-value pair)

print("====1. creating the empty dictionary===============")

person1 = {}
person2 = dict()

person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny',
           'cars':['audi', 'bwm', 'subaru', 'toyota']}



print("======2. accessing the value R==============")
##person1['name']
print(f"getting name of person1 '{person1['name']}'")

print(f"getting age of person1 {person1['age']}")

print("3. adding/updating key value pair to the dictionary (U)")
print('dictionary', person1) # before update
person1['phone'] = '929-645-1991'  # phone does not exist in keys, so it adds new key-value pair (element)
print('dictionary after update', person1)
print("                                                                                               "
      "")
print("updating the value of 'age' in the person1 dictionary.")
person1['age'] = 30  ### age is now updated to 30
print(person1)
print("                                                                                               "
      "")
print("updating the list value inside the dictionary")
#cars[0] = 'merc'
person1['cars'][0] = 'merc'
print('updated list (audi to merc) in personal dict: ', person1)

languages_list = ['eng', 'ru', 'esp', 'marsian']
person1['languages'] = languages_list
print(person1)
languages_list[3] = 'ger'
print('updated list: ', languages_list)
print('dictionary: ', person1)

#copying the list to a value of the dictionary (independent value)
#languages_list = ['eng', 'ru', 'esp', 'marsian']
#person1['languages'] = languages_list[:]
#print(person1)

print("=============4. Delete key-value pair from the dictionary (D)")
print("Deleting the location key-value pair from person1....")
del person1['location']
print("updated person1 dictionary: ", person1)
person1['age']  = None
print("updated person1 dictionary: ", person1)


print(""
      "Exercise : 6-2 Favorite Numbers")
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
#print each person's name and their fav number.
print(f"Nicole's fav number is: {fav_nums['nicole']}")
print(f"Alex's fav number is: {fav_nums['alex']}")
print(f"Yulia's fav number is: {fav_nums['yulia']}")

print("                                                                                                                                                                                             ")
print("HW 6-1, 6-3")


