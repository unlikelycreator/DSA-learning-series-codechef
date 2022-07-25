T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    L1 = sorted(A)
    L2 = [A.index(L1[0]),0]
    L3 = [0] * N
    for i in range(2):
        L2[0] = 0
        while L2[0] < N:
            if not L3[L2[0]] and A[L2[0]] == L1[L2[1]]:
                L3[L2[0]] = 1
                L2[0] += 1
                L2[1] += 1
            else:
                L2[0] += 1
    print("YES" if L2[0] == L2[1] else "NO")