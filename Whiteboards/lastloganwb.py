# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

# Example input:
movie_lengths1=[20, 30, 110, 40, 50]
flight_length=160
# Example output:
True

# Example input:
movie_lengths2=[80, 110, 40]  #false
flight_length=160
# Example output:
False

def solution(target,nums,):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return True
    return False

