month=int(input("enter the month"))
date=int(input("enter the date"))
year=int(input("enter te year"))
match=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
try:
    if(date<=31)and (month<=12):
        year=year-(14-month)/12
        x=year+year/4-year/100+year/400
        month=month+12*((14-month)/12)-2
        day=int((date+x+31*month/12)%7)
        print(day)
        print(match[day])
    else:
        print("enter correct date and month")
except NameError as e:
    print(e)
