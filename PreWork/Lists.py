#follow along lists but dnd instead of names/transport
#3.1 and 2 combined
character_class = ['fighter','wizard','thief','cleric']
print("Greetings Noble " + character_class[0].title())
print("Greetings Noble " + character_class[1].title())
print("Greetings Noble " + character_class[2].title())
print("Greetings Noble " + character_class[3].title())


print("\n\n")
#3.3 Custom messages
print("I prefer for my " + character_class[0] + "s to be halflings for fun!")
print("I generally don't play my " + character_class[1] + "s as anything but controllers.")
print("A bad " + character_class[2] + " can ruin a good campaign")
print("Having atleast 1 " + character_class[3] + " is essential, \nand are even better if elven!")

#3.4  Guest list, fantasy edition
fellowship = ['gandalf','aragorn','gimmli']
print('Dearest ' + fellowship[0].title() + ', I am hosting a gathering of heroes this Friday\nand would be greatly pleased with your company')
print('Hail ' + fellowship[1].title() + ' the riders of Rohan and myself would like to invite you to a celebratory banquet this Friday!')
print(fellowship[2].title() + ', I have a keg of Stormtout Ale and a whole hog waitin for ye this Friday!')
print('\n\n')
#3.5
fellowship[0] = 'legolas'
print('Dearest ' + fellowship[0].title() + ', I am hosting a gathering of heroes this Friday\nand would be greatly pleased with your company!')
print('Hail ' + fellowship[1].title() + ' the riders of Rohan and myself would like to invite you to a celebratory banquet this Friday!')
print(fellowship[2].title() + ', I have a keg of Stormtout Ale and a whole hog waitin for ye this Friday!')

#3.6 Inserting guests, formalizing as well the invite
print('\n-------------------------\n')
invite_text = ', you are cordially invited to my BBQ this Friday!'

fellowship.insert(0,'gandalf')
fellowship.insert(2,'samwise')
fellowship.append('frodo')

print(fellowship[0].title() + invite_text)
print(fellowship[1].title() + invite_text)
print(fellowship[2].title() + invite_text)
print(fellowship[3].title() + invite_text)
print(fellowship[4].title() + invite_text)
print(fellowship[-1].title() + invite_text)

#3.7 NO table POP exercise
rainchk = ' sadly I cannot fit you for dinner'
print('---------------\n\nI have terrible news, my table has not arrived!')

guest = fellowship.pop()
print(guest.title() + rainchk)
guest = fellowship.pop()
print(guest.title() + rainchk)
guest = fellowship.pop()
print(guest.title() + rainchk)
guest = fellowship.pop()
print(guest.title() + rainchk)

print(fellowship[0].title() + invite_text)
del fellowship[0]
print(fellowship[0].title() + invite_text)
del fellowship[0]

print('\n\n----------------------------------')
#3.8 five places to visit
places = ['Cairo','London','Budapest','Prague']

print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print('\n\n-------------------------------')

#3.9
fellowship.append('gandalf')
fellowship.append('legolas')

print(str(len(fellowship)) + ' guests are coming for dinner this Friday.')

#3.10 Super list, Spellbook!



