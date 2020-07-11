class stack:
    def __init__(self):
        self.my_stack = []

    def push(self, data):
        return self.my_stack.append(data)

    def pop(self):
        return self.my_stack.pop()

s = stack()
for i in range(0,10):
    s.push(i)
    print(f'Stack after adding {i+1} element: {s.my_stack}')
num = int(input('Enter number between 1 and 9 :'))
for j in range(0,num):
    s.pop()
    print(f'Stack after removing {j+1} element: {s.my_stack}')


