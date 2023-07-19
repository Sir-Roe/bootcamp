# Mary brought home a "spot the differences" book.
# The book is full of a bunch of problems, and each problem consists of two strings that are similar.
# However, in each string there are a few characters that are different. An example puzzle from her book is:
# String 1: "abcdefg"
# String 2: "abcqetg"
# Notice how the "d" from String 1 has become a "q" in String 2, and "f" from String 1 has become a "t" in String 2.
# It's your job to help Mary solve the puzzles. Write a program spot_diff/Spot
# that will compare the two strings and return a list with the positions where the two strings differ.
# In the example above, your program should return [3, 5] because String 1 is different from String 2 at positions 3 and 5.
# NOTES:
# • If both strings are the same, return []
# • Both strings will always be the same length
# • Capitalization and punctuation matter



#SPOT difference btwn 2 strings using a function pass 2 sts
#returning a list of differences at the index
string1= 'abc'
string2= 'abc'
#my_list=[]

#for i in range(len(str1)):
 #   if str1[i] != str2[i]:
  #      list.append(i)

#return [i for i in range(len(str1)) if str1[i] != str2[i]]

def spot(str1:str,str2:str):
    return [i for i in range(len(str1)) if str1[i] != str2[i]]

print(spot(string1,string2))



