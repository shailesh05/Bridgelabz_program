def string_insert():
    size = int(input("enter the size"))
    list1=[]
    for i in range(size):
        val=input("enter the word")
        list1.append(val)
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while (j>=0) and (temp<=list1[j]):
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=temp
    print(list1)



string_insert()