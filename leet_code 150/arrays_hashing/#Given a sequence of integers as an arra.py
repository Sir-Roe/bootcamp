#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
#Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.
#Example
#For sequence = [1, 3, 2, 1], the output should be
#solution(sequence) = false.
#There is no one element in this array that can be removed in order to get a strictly increasing sequence.
#For sequence = [1, 3, 2], the output should be
#solution(sequence) = true.
#You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

#iterate through a list? add a counter for if condition? strictly increasing

def seq(lst):
    c = []

    for i in range(len(lst)-1):
        if lst[i+1] <= lst[i]:
            c.append(i+1)
    print(c)
    print(len(c))
    if len(c)>1:
        return False
    elif len(c)==1:
        del lst[c[0]]
        print(lst)
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                return False
    return True


sequence = [105,924,32,968]
print(seq(sequence))
