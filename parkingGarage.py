class parkingGarage():

    def __init__(self,payment,parkingSpaces,tickets):
        self.payment = payment
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets
   
     # Get Ticket
    def takeTicket(self):
        if self.parkingSpaces == []:
            print('Please wait, the garage is full.') 
        else:
            print(f'This is your parking spot: {tickets[-1]}')
            user_ticket = self.tickets.pop()
            return user_ticket
            user_space = self.parkingSpaces.pop()
            return 
   
    # Leave
    def leaveGarage(self):
        if self.payment == 'paid':
            print('Thank you, have a nice day!')
            tickets.append()
            parkingSpaces.append()
        else:
            pay_now = input('Please enter your payment to leave.')
            return pay_now
            if self.payment == 'paid':
                print('Thank you, have a nice day!')

    # Pay for Parking
    def payForParking(self):
        if paid = True:
            print('You have 15 mins to leave')
        else:
            self.payment = input('Please enter your payment: ')
            currentTicket[ticket] = 'paid'
    

tickets = [1,2,3,4,5,6,7,8,9,10]
parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
currentTicket = parkingGarage({ticket: paid})

def start_Garage():
    while True:
        print('What do you want to do?')
        response = input('Choose one of the following: Ticket/Pay/Leave ')
        if response == 'Ticket' or 'ticket':
            currentTicket.takeTicket()
        elif response == 'Pay' or 'pay':
            currentTicket.payForParking()
        elif response == 'Leave' or 'leave':
            currentTicket.leaveGarage()
            break
        else:
            print('Please enter a valid input.')

start_Garage()