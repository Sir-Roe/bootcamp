'''
Welcome to Logan's Garage.
This is a small parking garage for boutique shopping center
in Oak Park illinois. We can hold 100 cars at one time.
Parking is a fair $10 flat fee and is CARD ONLY. 
We are not a 24/7() garage. We are open from 06:00-22:00, 
and tow all  remaining cars over night. This is done for 
the safety and cleanliness of the garage, 

thank you for understanding!
update

'''
class ParkingGarage():
    def __init__(self) -> None:
        self.tickets ={}
        self.parkingSpace = 100
        self.sales = 0.
        self.Open = False
        self.parkMax = 100

    def openBusiness(self):
        self.Open = True
        self.parkingSpace = self.parkMax

    def takeTicket(self):
        #this will generate the ticket logic, determine if
        #there is space in the garage for the driver or let 
        #them know there is no space and apologize for the inconvenience
        #generate new ticket for the parker!
        if self.Open == True:
            if self.parkingSpace > 0:
                self.parkingSpace -= 1
                print("Your ticket number is LG#" + str(len(self.tickets)+1))
                self.tickets['LG#'+ str(len(self.tickets)+1)] = False
            else:
                print('Sorry we are currently at Capacity')
            #adding a new key id /ticket num based on increments
        else: print('Sorry we are closed!')  


    def payForParking (self,ticketnum: str):
         if ticketnum  in [i for i in self.tickets]:  
            if self.tickets[ticketnum] == False:
                while True:
                        #convert this to string to avoid errors thrown but still loops
                        amt =input('Please type "10", to confirm your 10 dollar charge     :')
                        if  str(amt) == '10': 
                            self.tickets[ticketnum] = True
                            print(f'Your ticket :"{ticketnum}" has been paid, you have 15 minutes to leave!')
                            self.sales += 10.00
                            break
            else:
                print(f'{ticketnum} is already paid!')
         else:
            print('Invalid Ticket, if you lost your ticket, please fay the penalty fee at the gate')
                
    def leaveGarage(self,ticketnum: str):
        #check if the ticket inserted is valid and PAID
        if ticketnum.upper()  in [i for i in self.tickets]:
            if self.tickets[ticketnum] == True:
                self.parkingSpace += 1
                del self.tickets[ticketnum]
                print("Please drive forward, Enjoy your day")
            else:
        #if it isn't paid prompt the paying of the ticket!        
                print("please insert your card and enter payment value here")
                self.payForParking(ticketnum)
                del self.tickets[ticketnum]
        else:
        #if the ticket is invalid or unreadable ask for the confirmation
        #on the lost ticket $20 charge
            while True:
                request = input('Ticket lost?: Please enter "y" to pay $20 lost ticket fee to exit : ')
                if request.lower() == 'y':
                    self.parkingSpace += 1
                    print("Please drive forward, Enjoy your day")
                    self.sales += 20.00
                    break

    def viewSales(self):
        print(f'You have made $' + str(self.sales) + ' in parking sales today!')
          
    def closeBusiness(self):
        self.tickets ={} #clear the ticket cache 
        print('There were ' + str(self.parkMax-self.parkingSpace) + ' cars towed!')
        self.parkingSpace = self.parkMax #tow all cars 
        self.Open = False
        self.viewSales()
        
#------------------------------------------Testing---------------------------------------------------------#

logans_lot = ParkingGarage()

logans_lot.openBusiness()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.takeTicket()
logans_lot.payForParking('LG#2')
#shows you cannot double pay for a ticket
logans_lot.payForParking('LG#2')
logans_lot.leaveGarage('LG#2')
#invalid ticket triggers lost ticket when you try to leave the garage
logans_lot.leaveGarage('LG#15')
#cannot use the same ticket twice to leave the garage
#this will trigger the lost ticket at the garage leave function
logans_lot.leaveGarage('LG#3')
logans_lot.leaveGarage('LG#3')
logans_lot.closeBusiness()