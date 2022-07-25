global fac,inv,finv, Mod
fac=[0]*1000001
inv=[0]*1000001
finv=[0]*1000001
Mod=998244353

def C(x,y):
    if(x<0 or y>x):
        return 0
    return fac[x]*finv[y]%Mod*finv[x-y]%Mod

if __name__ == "__main__":
    fac[0] = inv[0]=inv[1]=finv[0]=finv[1]=1
    for i in range(1,1000001):
        fac[i]=fac[i-1]*i%Mod
    
    for i in rnage(2,1000001):
        inv[i]=Mod-Mod//i*inv[Mod%i]%Mod

    for i in range(2,1000001):
        finv[i]=finv[i-1]*inv[i]%Mod

    T = int(input())
    while(T):
        c0 = c1 = a = 0
        N = int(input())
        lis = [int(i) for i in input().strip().split(' ')]

        for i in range(N):
            if (lis[i] == 0):
                c0 += 1
            else:
                c1 += 1
        
        for i in range(c1 + 1):
            a = (a+i*C(c1+c0-i,c0))%Mod
        
        ans = (((a*(c0+1)-C(c1 + c0-2,c0-1))%Mod+Mod)%Mod+C(c1+c0-2,c0-1))*fac[c1]%Mod*fac[c0]%Mod
        print(ans)
        T -= 1