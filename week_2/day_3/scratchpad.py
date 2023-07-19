'''
### **Task 1: Build a Shopping Cart**
**You can use either lists or dictionaries. The program should have the following capabilites:**
* Takes a string as an input
* Stores user input in a dictionary or list
* Users should be able to:
    * Add Items
    * Delete Items
    * See current shopping cart
* The program should loop until user 'quits'
* Upon quitting the program, print out all items in the user's list
'''
#def shopper ():
#cart={}
#action= input('Please type "add","delete","view","clear", or "finish" your shopping cart')

        

   # pass



def getaddress():
    cart={}
    while True:
        action= input('Please type "add","delete","view","clear", or "finish" your shopping cart')

        if action.lower() == 'finish':
            for key,value in d.items():
                print(f"{key} lives in {value}")
            break
        elif action.lower() == 'add':
            item =input('Name of the item you would like? ')
            qty = input('How much of this item would you like? ' )
            cart[item.lower()] = qty.lower()
        elif action.lower() == 'view':
            print(f"{key} : {value}" for key,value in cart.items())
        elif action.lower() == 'clear':
            cart.clear()
        elif action.lower() == 'delete':
            try:
                del_inp = input('Which Item would you like to delete? ')
                del cart[del_inp.lower()]
            except:
                print("This item does not exist, check again from your below items")
                print(f"{key} : {value}" for key,value in cart.items())
        else:
            print('You need to input a VALID answer, try "add","delete","view","clear", or "finish"')
getaddress()
   