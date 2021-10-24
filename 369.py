a=int(input())
game=['3','6','9']

for i in range(1,a+1):
    count=0
    for j in str(i):
        if j in game:
            count+=1
    if count>0:
        i='X'*count
    print(i)