a=[1,5,15,7,3]
for i in range(1,len(a)):
    j=a[i]
   # print(j)
    pos=i
   # print(pos)
    while pos>0 and a[pos-1]>j:
            a[pos]=a[pos-1]
            pos=pos-1
    a[pos]=j
print(a)