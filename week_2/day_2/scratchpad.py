a = [1, 2, 3, 3, 5, 9, 6, 2, 8, 5, 2, 3, 5, 7, 3, 5, 8]
b = []
[b.append(item) for item in a if item not in b]

print(b)




first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Richards', 'Williams', 'Bell']

def full_name(f_name:list,l_name:list):
    f_l_name=[]
    for index in range(len(f_name)):
        f_l_name.append(str(f_name[index]) + ' ' + str(l_name[index]))

    return f_l_name

print(full_name(first_name,last_name))