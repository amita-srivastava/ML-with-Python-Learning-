stack = []
for i in range(0,10):
    stack.append(i)
    print(f'Stack after adding {i+1} element: {stack}')
num = int(input('Enter number between 1 and 9 :'))
for j in range(0,num):
    stack.pop()
    print(f'Stack after removing {j+1} element: {stack}')

