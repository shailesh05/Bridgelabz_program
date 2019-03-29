import  time
start=input("press enter the start the timer")
print ("timer has start")
begin=time.time()
print(begin)
end=input("press enter to stop timer")
ender=time.time()
print(ender)
elapsed=ender-begin
elapsed=float(elapsed)
print(elapsed,"sec")





