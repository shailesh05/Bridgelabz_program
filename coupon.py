import random
def coupon(n):
    count=0
    a=[]
    while len(a)<n:
        r_num=random.randint(1,n)
        count=count+1
        if r_num not in  a:
            a.append(r_num)
    print(count)
    print(a)
n=100
coupon(n)
