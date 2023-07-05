
print("----------------\nQuestion1\n----------------")
#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has #been defined as below.

def hello_name(user_name):
        print('Hello ' + user_name +'!')

hello_name('Logan')

print("\n----------------\nQuestion2\n----------------")
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    odd_num = list(range(1,100,2))
    print(odd_num)
first_odds()


print("\n----------------\nQuestion3\n----------------")
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the #code has been defined as below.
my_list=list(range(1,43))

def max_num_in_list(a_list):
     return max(a_list)

biggest_num = max_num_in_list(my_list)

print(biggest_num)
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by #100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#    def is_leap_year(a_year):
#        .....
                
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are #consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#    def is_consecutive(a_list):
#        .....