#function_filter_list.py

def function(input_list, threshold): #two parameters - the list to be modified, and the threshold to evaluate the function against 
    return [item for item in input_list if item > threshold] #this tells the function to return anything about the threshold

input_list = [1,2,3,4,5,6,7,8,9] #this is the input
function(input_list, 5) #the threshold is 5