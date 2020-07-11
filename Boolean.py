def my_boolean(x):
    if x == 'False' or x == 0:
        return False
    else:
        return True

inpt = input('Enter any value :')
print(inpt)
print(my_boolean(inpt))

