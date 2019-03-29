def vending_machine(rs):
	money=[1000,500,100,50,20,10,5,2,1]
	note=0
	for i in range(len(money)):
		if rs //money[i]>0:
			print(money[i],rs//money[i])
			note=note+(rs//money[i])
			rs=rs%money[i]
        print(note)

