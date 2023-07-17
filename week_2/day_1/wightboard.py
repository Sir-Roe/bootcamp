'''
Normally we have firstname, middle and the last name but there may be more than one word in a name like a South Indian one.
Similar to those kinda names we need to initialize the names.
See the pattern below:

initials('code wars') => returns C.Wars
initials('Barack Hussain obama') => returns B.H.Obama
Complete the function initials.


Names are separated by exactly one space in the input, without leading or trailing spaces. Names will always be lowercase, except optionally their first letter.
'''


#focus solely on the gathering of info of the question and write down anything of importance

#Step1 understand:
# We will be working with first, mid, last name. Need to abbreve First,Middle and return last full, all need to be title case no spaces

#Step 2: Plan:
#split the string into a list object, spaces = new name,if value is the last value in the string, last word is last word with space before 










#Step 3: execute: 
def initials(name):
    word_list=name.split()
    new_names = []

    for word in word_list:
        if  word == word_list[-1]:
            new_names.append(word.title())
        else:   
            new_names.append(f'{word[0].upper()}.')
    return ''.join(new_names)


print(initials('Logan machail roe'))

#Step 4: Refactor

def initials(name):
    return ''.join([word.title() if word==name.split()[-1] else f'{word[0].upper()}.' for word in name.split()])

print(initials('Logan machail roe'))


is_p =input('type p or somethin idc my bff jill? ')
check_p =False

for c in is_p.lower():
    if c == 'p':
        check_p = True

print(check_p)