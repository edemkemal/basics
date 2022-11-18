alien_color = 'blue'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")
else:
    print("You just earned 0 points")


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")

else:
    print("We need to find some users!")

    for i in range(1, 101):
        # check if number is divisible by both 3 and 5
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        # check if number is divisible by 3
        elif (i % 3 == 0):
            print("Fizz")
        # check if number is divisible by 5
        elif (i % 5 == 0):
            print("Buzz")
        # if not divisible by either of them print the i
        else:
            print(i)

