def rec_n(n, start=1):
    print(start)
    if start < n: 
        rec_n(n, start + 1)
par = int(input())
rec_n(par)

