t = int(input())
for i in range(0,t):
    inp = input()
    li = inp.split()
    y = int(li[0])
    x = int(li[1])
    m = max(x,y)
    diag = m*(m-1)+1
    if(diag%2==0):
        if(x<y):
            diff = y-x
            print(diag+diff)
        else:
            diff = x-y
            print(diag-diff)
    else:
        if(x<y):
            diff = y-x
            print(diag-diff)
        else:
            diff = x-y
            print(diag+diff)