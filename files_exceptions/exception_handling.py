##Python uses special objects called exceptions to manage errors that arise
# during a program's execution

try:
    #usual code to execute

    print('executing a code in try block')
    #print(9/0) # division by 0 error

    filepath2 = '../data/samplse.txt'

    with open(filepath1) as prod_list:
        contents = prod_list.read()
        print("Contents of the file: \n", contents)



except ZeroDivisionError:
    # executes only when ZeroDivisionError happens
    print("You can not divide by 0!")
except FileNotFoundError:
    print("oops, no file no code execution")
except Exception as err:
    print('printing the standard error', err)
finally: # you dont have to use this block
    #this block will be executed regardless exceptions happen or not
    print("clean up and close the browser.")

print("Execution completed !!!")

#H/W 10-8