reverse_string=""
def sort_dict_by_even_odd(data):
    """Sorts a dictionary by value, placing even values first in ascending order, 
    and odd values at the end in ascending order.
    """
    even_items = {k: v for k, v in data.items() if v % 2 == 0}
    odd_items = {k: v for k, v in data.items() if v % 2 != 0}

    sorted_even = dict(sorted(even_items.items(), key=lambda item: item[1]))
    sorted_odd = dict(sorted(odd_items.items(), key=lambda item: item[1]))

    return {**sorted_even, **sorted_odd}

def helper(dict_of_chars,list_of_chars,ind):
    global reverse_string
    if(ind>=len(list_of_chars)):
        return
    char = list_of_chars[ind]
    count = int(dict_of_chars[char])
    if(count%2==1):
        reverse_string=reverse_string+char*(count)
    else:
        reverse_string=reverse_string+char*(count//2)
        helper(dict_of_chars,list_of_chars,ind+1)
        reverse_string=reverse_string+char*(count//2)

def builder(dict_of_chars):
    global reverse_string
    helper(dict_of_chars,list(dict_of_chars.keys()),0)
    return  reverse_string
    

def is_valid(dict_of_chars):
    count_of_odds = 0
    list_of_values=list(dict_of_chars.values())
    for i in list_of_values:
        if(i%2==1 or count_of_odds>1):
            count_of_odds+=1
            if(count_of_odds>1):
                return False
    return True

input_str = input()
dict_of_chars = dict()

for i  in input_str:
    if(i not in dict_of_chars):
        dict_of_chars[i] = 1
    else:
        dict_of_chars[i] = dict_of_chars[i]+1
if(is_valid(dict_of_chars)):
    sorted_dict = sort_dict_by_even_odd(dict_of_chars)
    print(builder(sorted_dict))
else:
    print("NO SOLUTION")


        


