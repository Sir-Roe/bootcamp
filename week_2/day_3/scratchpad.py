i=0
def make_looper(string):
    
    sqs=['a','b','c']
    if i > 2:
        i=0    
    else:
        i+=1    
    return sqs[i]

'''abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call'''
#print(make_looper)
#print(make_looper)
print(make_looper)


sqs=['a','b','c']
print(sqs[i])
