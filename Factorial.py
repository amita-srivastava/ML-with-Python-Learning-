def recur(n):
    if n == 1:
        return n
    else:
        return n * recur(n-1)

num = int(input('Please enter an integer: '))
factn = 1
for i in range(num,1,-1):
    factn *=i
print(f'Factorial of {num} using non-recursive: {factn}')

print(f'Factorial of {num} using recursive: {recur(num)}')



