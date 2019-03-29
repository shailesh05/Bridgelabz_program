import random
def gamebler(stake,goal,ntime):
    win=0
    loss=0
    bet=0
    for i in range(ntime):
        r_num=random.randint(0,10)
        while stake>0 and stake<goal:
            bet=bet+1
            if r_num<5:
                stake=stake+1
            else:
                stake=stake-1
            if stake==goal:
                win=win+1
            else:
                loss=loss+1
         #  print(win)
          # print(loss)
    print("win p",(win*100)/ntime)


gamebler(100,500,12)
