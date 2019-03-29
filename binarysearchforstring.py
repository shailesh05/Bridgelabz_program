n = int(input("enter the  size"))
a = []
b = []
for i in range(n):
    user = input("enter the word")
    a.append(user)
    b = sorted(a)
print(b)
low = 0
high = len(b) - 1
target = input("enter the target word")
while low <= high:
    mid = (low + high) // 2
    if b[mid] == target:
        print(mid)
        break
    elif b[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
else:
    print(target,"not in list")


# print(target,"false")
