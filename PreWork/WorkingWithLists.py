##Chapter 4
print('Ch. 4# working with lists')


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 print("I can't wait to see your next trick, " + magician.title() + ".\n")

 print("Thank you everyone, that was a great magic show!")

 squares = []
for v in range(1,11):
    squares.append(v**2)
print(squares)
