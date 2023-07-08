alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
 # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
     }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

#6-1
print('\n6.1\n--------------------')
Bilbo = {
    'first_name' : 'Bilbo',
    'Last_name' : 'Baggins',
    'age' : 111,
    'height' : 1.25,
    'location':'the Shire'
    ,'items':{
        'sword':'sting',
        'armor':'mithril tunic',
        'trinket':['the One Ring','bag of holding','compass']
        }
    }
print(Bilbo['first_name'])
print(Bilbo['Last_name'])
print(Bilbo['age'])
print(Bilbo['location'])

#6-2

print('\n6.2\n--------------------')

Fav_Num = {
    'Logan':410,
    'Lily' :8,
    'Mony' :21,
    'Cam'  :420,
    'Chief':600,
    'Jonny':40
}

Fav_Num['Logan'] = 20
print(Fav_Num)
#looping 
for name, num in Fav_Num.items():
    print(name.title() + "'s fav Num is " + str(num))
#looping through keys to find Keys    
if 'Jonny' not in Fav_Num.keys():
    print('Jonny, take the damn poll')
#looping through Values to find
print('\nThe Following Nums are Fav')
for num in Fav_Num.values():
    print(num)
    
Bilbo = {
    'first_name' : 'Bilbo',
    'Last_name' : 'Baggins',
    'age' : 111,
    'height' : 1.25,
    'location':'the Shire',
    'companions': ['Gandalf','Thorim','Balin']
    ,'items':{
        'sword':'sting',
        'armor':'mithril tunic',
        'trinket':['the One Ring','bag of holding','compass']
        }
    }

print('\nRandom Testing\n--------------------')

a_list=[]

for k ,v in Bilbo['items'].items():
        if k== "sword" or k=="armor":
             a_list.append(v)
print(a_list)
