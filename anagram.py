#user1=input("enter the string")
#user2=input("enter the string")
#x=sorted(user1)
#y=sorted(user2)
#if x==y:
 #   print("it is anagram")
#else:
 #   print("not anagram")
def ana(string1, string2):
    count=0
    if len(string1)==len(string2):
        for i in range(0, len(string1)):
           # print(i)
            for j in range(0, len(string2)):
                if string1[i] == string2[j]:
                    count = count+1
                    print(count)
                   # print(i)
                  #  print(j)
                    break
        if len(string1) == count:
            print("in is ang")
        else:
            print("not anagram")
    else:
        print("length is not match")
ana('abdc','badc')