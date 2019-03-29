a=[10,4,12,5,9,26,6]
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)