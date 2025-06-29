n = int(input())
inp = input()
st = inp.split()
num = [int(s) for s in st]
moves = 0
for i in range(1,len(num)):
    if(num[i-1]>num[i]):
        diff = num[i-1]-num[i]
        moves+=diff
        # since the element is now as same as previous element
        num[i] = num[i-1]
print(moves)