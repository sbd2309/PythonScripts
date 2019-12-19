class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        
        self.balance +=amount
        return "{} Amount Credited Successfully".format(self.balance)
    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance=self.balance-amount
            return "{} Amount Debited Successfully, Available Balance {}:".format(amount,self.balance)
        else:
            return "Insufficient Balance:"
i_account=Account("Soumya",0)
i=1
while i==1:
    t=input("d-Deposit w-Withdraw")
    if t=='d':
        amount=int(input("Deposit:"))
        print (i_account.deposit(amount))
    elif t=='w':
        amount=int(input("Withdraw:"))
        print (i_account.withdraw(amount))
    i=int(input("continue-1 exit-0"))    
