# You are given a list of integers. Write a function to find the two numbers that appear the
# most frequently in the list. If multiple pairs have the same frequency, return the pair with the smallest sum.
# For example, given the list [1, 2, 2, 3, 3, 4, 4], the function should return the pair [2, 3]
# because both numbers appear twice, and their sum is smaller than the sums of other pairs with the same frequency.
# Challenge: Cannot use the sorted function

def twocountSmallsum(nums):
    hashset= {k:nums.count(k) for k in nums}
    maxl= max([v[1] for v in hashset.items()])
    ans=[]
    while len(ans)<2:
        for k in list(hashset.keys()):
            if hashset[k] == maxl:
                ans.append((k,hashset.pop(k)))
        #reset max to account for new max,       
        maxl= max([v[1] for v in hashset.items()])

    #check for multiple maxes
    maxl=max([val[1] for val in ans])
    if [val[1] for val in ans].count(maxl) >1:
        while len(ans)>2:
            maxl=max([val[0] for val in ans])
            for i in ans:
                if i[0]==maxl:
                    ans.remove(i)
    
        
        return [i[0] for i in ans]
    else:
        print("MULTIMAX NOT FOUND")

print(twocountSmallsum([1,2,2,3,3,4,4]))
print(twocountSmallsum([4,4,4,2,2,3,3,1,]))

