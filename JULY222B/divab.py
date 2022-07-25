T= int(input())
for _ in range(T):
    A,B,N = map(int, input().split())
    if (A%B == 0):
        print(-1)
        continue
    else:
        i = N
        if (i%A != 0):
            i = N + A - (N%A)
        while not(i % A==0 and i % B != 0):
            i+=A
        print(i)
        