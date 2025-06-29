def solve(a,b):
    if(a<1 or b<1):
        return False
    if(a==1 and b==2):
        return True
    elif(a==2 and b==1):
        return True
    if(solve(a-1,b-2)):
        return True
    else:
        return (solve(a-2,b-1))
         
test = int(input())
for i in range(test):
    inp = input().split()
    num = [int(s) for s in inp]
    a = num[0]
    b = num[1]
    if(a<b):
        t = a
        a = b
        b = t
    if(a>2*b or (a+b)%3!=0):
        print("NO")
    else:
        print("YES")