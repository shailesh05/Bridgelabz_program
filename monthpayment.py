def monthpay():
    principle=float(input("enter the principle"))
    year=int(input("enter the year"))
    interest=float(input("enter the interest"))
    r=interest/(12*100)
    n=12*year
    payment=(principle*r)/(1-(1+r)**(-n))
    print(payment)
monthpay()
