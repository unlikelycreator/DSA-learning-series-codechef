"""from math import ceil
N = int(input())
cust = []
for i in range(N):
    bud = int(input())
    cust.append(bud)
cust.sort()
average = sum(cust)/len(cust)
ans = round(average, 2)
ans = ceil(ans)
out = 0
for i in range(N):
    if (cust[i]>=ans):
        out += ans
print(out)
print(ans)
"""
N=int(input())
cust=[]
for i in range(N):
    bud=int(input())
    cust.append(bud)
maxrev=[]
cust=sorted(cust)
for i in range(len(cust)):
    count=N-i
    maxrev.append(count*cust[i])
maxrev=sorted(maxrev)
print(max(maxrev))