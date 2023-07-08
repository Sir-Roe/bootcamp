#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has #been defined as below.

def hello_name(user_name):
        print('Hello ' + user_name +'!')


#my test data below
#hello_name('Logan')


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    odd_num = list(range(1,100,2))
    print(odd_num)

#code used to test below
#first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the #code has been defined as below.

def max_num_in_list(a_list):
     return max(a_list)

#this is my test below feel free to use it
#my_list=list(range(1,43))
#biggest_num = max_num_in_list(my_list)
#print(biggest_num)

#Question 4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by #100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        return True
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    else:
        return False
                
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are #consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.



def is_consecutive(a_list):
#variables for function, sort the list first
#used last num to track value of prior int, initialized as 0
    a_list.sort()
    iscon = True
    last_num = 0
    for i, item in enumerate(a_list):
        #if we are at the beginning we don't do anything but set the last_num var
        if i == 0:
            last_num = item
            continue
        elif item != (last_num)+1:  
            iscon = False
            break
        else:
            last_num = item
            
    return iscon

#i think for this to be really safe we would obviously need
#   a way to validate that list is infact full of integers
#   but since this wasn't a requirement I did not bother to add


#my test data to validate.
#a_list = [1,2,4,5]
#a_list = [2,4,3,5,6,7]
#print(is_consecutive(a_list))