#recursive_inner_plus.py
def recursion(input_list): #check to see if nothing is a list, if not, proceed
    if not any(isinstance(i, list) for i in input_list):
        return [x+1 for x in input_list]
#now we have the rules, just have to find the innermost list and apply the rules
    for i, elem in enumerate(input_list):
        if isinstance(elem, list): #recursively increment innermost list
            return recursion(elem)
            
input_list = [1,2,3,4,[5,6,7,[8,9]]]
answer = recursion(input_list)
print(answer)