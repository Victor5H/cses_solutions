
def solve(n,a,b,c):
    if(n>0):
        solve(n-1,a,c,b)
        print(a,b)
        solve(n-1,c,b,a)

n = int(input())
count = pow(2,n)-1
print(count)
solve(n,"1","3","2")
