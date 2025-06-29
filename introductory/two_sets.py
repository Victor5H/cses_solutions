n = int(input())
sum = (n*(n+1))//2
#if sum of first n numbers is not even
if(sum%2!=0):
    print("NO")
    
else:
    print("YES")
    set1 = set()
    set2 = set()
    nu = n-1
    switch = 1
    while(n>=1):
        if(switch==1):
            set1.add(n)
            n=n-3
            switch=0
        else:
            set1.add(n)
            n=n-1
            switch=1
    switch = 0
    while(nu>=1):
        if(switch==1):
            set2.add(nu)
            nu=nu-3
            switch=0
        else:
            set2.add(nu)
            nu=nu-1
            switch=1
    
    print(len(set2))
    for i in set2:
        print(i,end=" ")
    print()
    print(len(set1))
    for i in set1:
        print(i,end=" ")



