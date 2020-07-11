queue = []
for i in range(0,10):
    queue.append(i)
    print(f'Queue after adding {i+1} element: {queue}')
num = int(input('Enter number between 1 and 9 :'))
for j in range(0,num):
    queue.remove(queue[0])
    print(f'Queue after removing {j+1} element: {queue}')