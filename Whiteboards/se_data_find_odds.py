# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# constraints:
# cannot use .count()

#find odd count number WITHOUT using count, only 1 can be odd.


def oddtimes(lst):
    oddtimeset = set()
    
    for num in lst:
        if num in oddtimeset:
            oddtimeset.remove(num)
        else:
            oddtimeset.add(num)
    return oddtimeset.pop()

oddtimes(lst)
