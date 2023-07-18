'''
a = [1, 2, 3, 3, 5, 9, 6, 2, 8, 5, 2, 3, 5, 7, 3, 5, 8]
b = []
[b.append(item) for item in a if item not in b]

print(b)

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
n_list=[]
[n_list.append(name) for name in names if name not in n_list]

print (n_list)
##########
'''
'''
first_name = ['John', 'Evan', 'Jack', 'Max']
last_name = ['Picard', 'Williams', 'Daniels', 'Powers']

def full_name(f_name:list,l_name:list):
    f_l_name=[]
    for index in range(len(f_name)):
        f_l_name.append(str(f_name[index]) + ' ' + str(l_name[index]))

    return f_l_name

print(full_name(first_name,last_name))

first_name = ['John', 'Evan', 'Jack', 'Max']
last_name = ['Picard', 'Williams', 'Daniels', 'Powers']

def full_name2(f_name:list,l_name:list):
    return [(str(f_name[index]) + ' ' + str(l_name[index])) for index in range(len(f_name))]
    

print(full_name2(first_name,last_name))
'''

'''
l_1 = [1,5,4]
l_2 = [2,6,3]
list(set(l_1 + l_2))

print(sorted(l_1 + l_2))
'''
'''
first_names = ['andy','bre','brian','charlie','candy','marco','john', 'evan', 'jack', 'max']
middle_names =['fredrico','maria','christopher','donnie','fizzle','dany','andy', 'chuckles', 'tony', 'bologna']
last_names = ['johnson','marx','nolanson','kirkland','jenkins','roe','ironbrook','winchester','samuelson','boone']



def name_generator(fname:list,mname:list,lname:list):
    return [(str(fname[index]) + ' '+str(mname[index]) +' '+ str(lname[index])) for index in range(len(fname))]

print(name_generator(first_names,middle_names,last_names))
'''

def user_input():
    activ=[]
    while True:
        ask=input('What activities do you like? \n type "n" to quit')
        if ask.lower() == 'n':
            print(activ)
            break
        else:
            activ.append(ask)
        
user_input()
