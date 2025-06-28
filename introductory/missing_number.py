n = int(input())
inp = input()
st = inp.split()
li = [int(s) for s in st ]
sum_of_n = n*(n+1)/2
sum_of_input = sum(li)
print(int(sum_of_n-sum_of_input))
