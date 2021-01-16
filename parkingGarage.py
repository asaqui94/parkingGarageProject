class parkingGarage():

    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket=currentTicket
        
    

      # Get Ticket
    def takeTicket(self):
        if self.tickets == []:
            return 'Sorry, the garage is full'
        else:
            print('Your ticket is number: ',self.tickets[-1])
            self.tickets.pop(-1)
            print('Your allocated parking space is : ',self.parkingSpaces[-1])
            self.parkingSpaces.pop(-1)

   
   
    # Pay for Parking
    def payForParking(self):
        payment=''
        while payment == '':
            payment = input('Please enter any key to process your payment: ' )
            if payment != '':
                print('Your ticket has been paid. You have 15 mins to leave.')
                self.currentTicket['paid']=True
                return self.leaveGarage()
            else:
                continue
    
    # Leave
    def leaveGarage(self):
        if self.currentTicket['paid']==True:
            self.parkingSpaces.append(len(self.parkingSpaces)+1)
            self.tickets.append(len(self.tickets)+1)
            print('Thank You, have a nice day')
        else:
            self.payForParking()

tickets = [1,2,3,4,5,6,7,8,9,10]
parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
currentTicket={'paid':False}

car=parkingGarage(tickets,parkingSpaces,currentTicket)

def start_Garage():
    while True:
        print('What do you want to do?')
        response = input('Choose one of the following: Ticket/Pay/Leave ')
        if response.lower() == 'ticket':
            car.takeTicket()
        elif response.lower() == 'pay':
            car.payForParking()
        elif response.lower() == 'leave':
            car.leaveGarage()
            break
        else:
            print('Please enter a valid input.')

start_Garage()