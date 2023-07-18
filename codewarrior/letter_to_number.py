def alphabet_position(text):
    my_list= list(text.strip())
    newstr=''
    for item in my_list:
        x= ord(item)
        if x >= 65 and x <= 90:
            x=ord(item)-64
            newstr += str(x) + ' '
        elif x >= 97 and x <= 122:
            x=ord(item)-96
            newstr += str(x) + ' '
        else:
            continue
    if len(newstr)>0:
        y = int(len(newstr))-1
        newstr=newstr[0:y]   
    return newstr

print(alphabet_position(""))





