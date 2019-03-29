def permu(lst):
    if len(lst)==0:
        return []
    if len(lst)==1:
        return[lst]
    else:
        l=[]
        for i in range(len(lst)) :
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            print(xs)
            for p in permu(xs):
                l.append([x]+p)
               #print (p)
        return l
d=list("abc")
for p in permu(d):
    print(p)
