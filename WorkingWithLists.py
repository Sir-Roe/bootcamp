##Chapter 4

##4-1 Pizzas: Think of at least three kinds of your favorite pizza. Store these
##pizza names in a list, and then use a for loop to print the name of each pizza.
##•	 Modify your for loop to print a sentence using the name of the pizza
##instead of printing just the name of the pizza. For each pizza you should
##ave one line of output containing a simple statement like I like pepperoni
##pizza.
##•	 Add a line at the end of your program, outside the for loop, that states
##how much you like pizza. The output should consist of three or more lines
##about the kinds of pizza you like and then an additional sentence, such as
##I really love pizza!
print("-------------------------------------\n 4-1")
pizzas = ['calzone','Suasage','mushroom']
for pizza in pizzas:
    print(pizza.title() + ' is one of my favorite type of pizzas')
print('These are my top picks for pizza!')



<<<<<<< Updated upstream
 print("Thank you everyone, that was a great magic show!")

 squares = []
for v in range(1,11):
    squares.append(v**2)
print(squares)
=======

##4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
##print out the name of each animal.
##•	 Modify your program to print a statement about each animal, such as
##A dog would make a great pet.
##•	 Add a line at the end of your program stating what these animals have in
##common. You could print a sentence such as Any of these animals would
##make a great pet!


print('\n-----------------------------\n\n')
mystr=''
my_list = [2,2,3,4,5,6,7,8]
for member in my_list:
    if member == 2:
        break
    print(member, end=' ')
>>>>>>> Stashed changes
