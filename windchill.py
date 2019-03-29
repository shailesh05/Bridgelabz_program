import math
t=float(input("enter the temperature"))
v=float(input("enter the wind spped"))
if t>50:
    print("it is  not valid")
elif v>120 and v<3:
    print("it is not valid")
else:
    w=35.74+0.62*t+0.4275*t-35.75(math.pow(v,0.16))
    print(w)