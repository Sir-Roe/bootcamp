# The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it returns the number of positions where the input strings do not match.
# Examples:
# a = "I like turtles"
# b = "I like turkeys"
# Result: 3
# a = "Hello World"
# b = "Hello World"
# Result: 0
# a = "espresso"
# b = "Expresso"
# Result: 2
# Notes:
# You can assume that the two inputs are ASCII strings of equal length.


#Understand
#take two strings of equal lengths and see if they match

#plan   
#for loop go by each letter to see if they matych tne increase the number of error

#execute

def matching(str_1,str_2):
    return sum([1 for i in range(len(str_1)) if str_1[i] != str_2[i]])

print(matching('I like turtles','I like turkeys'))