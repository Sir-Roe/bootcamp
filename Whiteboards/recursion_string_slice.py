'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.
Example
For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''

#reverse string of characters, potentially with nested

input ="foo(bar)baz(blim)"
def solution(input):
    for index in range(len(input)):
        if input[index] == '(':
            strt=index
        elif input[index]== ')':
            end=index 
            #recursing through the solution
            
            return solution(input[:strt] + input[strt+1:end][::-1] + input[end+1:])
    return input
#the solution since it recurses evenly means one value is still not reversedm, this tripped YOU UP LOGAN
print(solution ("foo(bar(baz))blim"))


   
    

    


