def to_binary(n):
    bin_no=""
    for i in range(1,n):
        while n!=0:
            rem=n%2
            bin_no=str(rem)+bin_no
            n=n//2
            print(n)
    print(bin_no)
    
to_binary(10)
