l=2
h=1000
count=1
for num in range(l,h+1):
    for i in range(2,num):
        if (num%i)==0:
            count=0
            break

    else:
        print(num)
