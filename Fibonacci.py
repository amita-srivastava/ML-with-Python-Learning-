num = int(input('Enter any number: '))
a = 1
b = 1
print(a, end = '  ')
print(b, end = '  ')
for i in range(0,num):
    temp = b
    b = b + a
    a = temp
    print(b, end = '  ')