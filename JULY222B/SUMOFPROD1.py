from itertools import groupby
def groups(l):
   return [sum(g) for i, g in groupby(l) if i == 1]
T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out = groups(A)
    ans = 0
    for i in range(0,len(out)):
        x = out[i]
        ans += x*(x+1)/2
    print(int(ans))
