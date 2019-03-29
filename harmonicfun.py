def nth_harmonic(n):
    harmonic=1.0
    for i in range(2,n+1):
        harmonic=harmonic+1/i
    return harmonic
n=8
print(nth_harmonic(n))