def newton():
    try:
        c=int(input("enter the c"))
        t=c
        epsilon=1e-15
        while abs(t-c/t) >epsilon*t:
            t=(c/t+t)/2
        print(t)
    except ValueError as a:
        print(a)
        print("enter integer value")
newton()
