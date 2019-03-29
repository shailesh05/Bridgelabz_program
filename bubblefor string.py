def bubble_string():
    size = int(input("enter the size"))
    a = []
    for i in range(size):
        user = input("enter the element")
        a.append(user)
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
bubble_string()