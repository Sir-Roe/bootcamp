

def do_something(a_list):
    my_str=''
    for ran in a_list:
        my_str+=ran[0]
    return my_str
al_char = ['jaz','al','fazahl','abu']

print(do_something(al_char))