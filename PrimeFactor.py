num = int(input('Enter any number: '))
fact =[]
for i in range(1,num+1):
    if num % i == 0:
        fact.append(i)
print(fact)
count = 0
pfact = []
for j in fact:
    #print(j)
    count = 0
    for k in range(1,j+1):
        if j % k ==0:
            count += 1
            #print(f'count is: {count}')
    if count == 2:
        pfact.append(j)
if len(pfact)==0:
    print(1)
else:
    print(max(pfact))