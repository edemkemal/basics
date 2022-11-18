# CHAPTER 5: ELIF STATEMENTS
# ELSE IF >> ELIF

#if expression1:
#    code to execute when expression1 is True
#elif expression2:
#    code to execute when expression2 is True
#elif expression3:
#    code to execute when expression3 is True
#elif expression4:
#    code to execute when expression4 is True
#else:
#    code to execute when none of the above expressions are True

age = 300000
# if age is less than 17 then you can not get a drivers lisense, from 17-25 pay more for insurance
# older than 25 print dont drink and drive

# Q: if older than 25 print dont drink and drive, from 17-25 get dl but you will pay more to insurance
# age is less than 0-17 then you can not get a DL

if age<17:
    print('sorry, you still young, you can not get a DL, just play PlayStation')
elif age >= 17 and age < 25:
    print('Good, you are eligible to get a DL, but you will pay more for car insurance')
else:
    print('Great, if you have DL, please do not Drink&Drive or Smoke&Drive ')