inp = input()
count=1
ma =1
# marking as 1 since a char is occuring at least once
for i in range(1,len(inp)):
    if(inp[i-1]==inp[i]):
        count+=1
    else:
        if(count>ma):
            ma = count
        count=1
print(max(ma,count))