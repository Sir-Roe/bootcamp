import re

with open(r'C:\Users\Logan\Documents\GitHub\bootcamp\week_3\regex_test.txt') as f:
    data = f.read()
    f.close()

my_list =data.split('\n')
pattern= re.compile('([A-Z][a-zA-Z-a-z]+)\S(["..\."]\w|[A-Z]?\.?) ([A-Z][A-Za-z]+)')

for name in my_list:
    print(pattern.findall(name))
 
