n = int(input())
for i in range(1,n+1):
    total_possible = i*i*(i*i-1)/2
    attacking_combi = 4*(i-1)*(i-2)
    non_attack = total_possible - attacking_combi
    print(int(non_attack))

'''
number of attcking combination is derived from the number of 3X2 and 2X3 grid found in nXn input matrix
i.e. the number id 3X2 grid will be (n-1)*(n-2) and since 2X3 will also have sam occurence will multiply it by 2
and since there can be 2 knights positions placed in those grid again multiplying it by 2
hence making it 4*(n-1)*(n-2)
'''
