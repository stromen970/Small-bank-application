import sys
class customer:
    bankname="CANARABANK"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance + amt
        print('Now your bank balance is:',self.balance)
    def withdrawal(self,amt):
        if (amt > self.balance):
            print('Insufficient funds........... so we cant proceed this operation')
            sys.exit()
        else:
            self.balance=self.balance-amt
            print('After withdrawal your bankbalance is:',self.balance)
            print(amt,'Will be debited from your bank')
    def balanceenqueary(self,amt):
        print('Your bank balance is:',self.balance)
    

print('Welcome to',customer.bankname)
name=input('Enter account holder name:')
c=customer(name)
while(True):
    print("d-Deposit\nw-Withdrawal\nb-balanceenqueary\ne-exit")
    option=input('enter your option:')
    if(option.lower()=='d'):
        amt=float(input('Enter how much amount did you deposit:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('Enter how much amount did you withdrawal:'))
        c.withdrawal(amt)
    elif option=='b' or option=='B':
        c.balanceenqueary(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking....................:)")
        sys.exit()
    else:
        print('Choose valid option from above!!!!!!')




