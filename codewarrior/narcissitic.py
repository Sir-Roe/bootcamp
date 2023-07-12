def narcissistic( value ):
    
    num_c=len(str(value))
    narcos=[]
    narc_val=0
    for i, c in enumerate(str(value)):
        narcos.append(int(c))

    for i in narcos:
        narc_val+= i**num_c
        
    if narc_val==value:
        return True
    else:
        return False
    
print (narcissistic(7))

