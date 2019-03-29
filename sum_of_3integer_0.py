def sumzero(arr,n):
     for i in range(0,n-2):
         for j in range(i+1,n-2):
             for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    print(arr[i],arr[j],arr[k])
arr=[0,-1,2,-3,1]
n=len(arr)
sumzero(arr,n)