n = int(input())
for i in range(1,n+1):
    total_possible = i*i*(i*i-1)/2
    attacking_combi = 4*(i-1)*(i-2)
    non_attack = total_possible - attacking_combi
    print(int(non_attack))
