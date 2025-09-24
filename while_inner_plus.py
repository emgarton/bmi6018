#while_inner_plus.py
input_list = [1,2,3,4,[5,6,7,[8,9]]]

#aim is to return the innermost list [8,9] + 1, so [9,10]
def while_loop(input_list):
    current = input_list
    while any(isinstance(i, list) for i in current): #keep doing this until you get through all the nested lists
        for i in current:
            if isinstance(i,list): #checks if it is still a list,
                current = i 
                break #now we're in the innermost list so we can be done and just increment both elements by 1
    return [x+1 for x in current]

answer = while_loop(input_list)
print(answer)