mod = 1000000007
n = int(input())
ans = 1
for i in range(n):
    ans=ans*2
    ans = ans%mod
print(ans)
