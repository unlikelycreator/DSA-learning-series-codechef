import sys
MIN_INT = -sys.maxsize - 1
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A,B = 0,0
    if (M<2*N):
        print(M,M)
    elif(M%N == 0):
        print(M,N)
    else:
        x = M/2
        if (M>=2*N):
            x = 2*N
        diff = MIN_INT
        for i in range(N,x):
            d = int(M/i)
            dd = (i*d)-i
            if dd>diff:
                A = i
                B = i*d
                diff = dd
            N +=1
        print(A,B)

        



"""
for i in range(M):
    M = M-1
    if (M%N == 0):
        print(N,M)
        break
    else:
        N = N+1
        if (M%N == 0):
            print(N,M)
            break
"""