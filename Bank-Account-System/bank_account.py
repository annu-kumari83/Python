class BankAccount:
    def __init__(self ,name, account_number, balance):
        self.name=name
        self.account_number=account_number
        self.__balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance=self.__balance+amount
        else:
            print("Invalid deposit amount")
        
    def withdraw(self, amount):
        if amount<=0:
            print("Invalid withdraw amount")
        elif amount<=self.__balance:
            self.__balance=self.__balance-amount
        else:
            print("insufficient balance")
        
    def check_balance(self):
        print("Your current balance is:",self.__balance)
        
    def show_details(self):
        print("Name:",self.name)
        print("Account Number:",self.account_number)
        print("Balance:",self.__balance)
        
b = BankAccount("Annu",1456,5000)


#Main Menu
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Show Details")
    print("5.Exit")
    
    choice = input("Enter your choice : ")
    
    #Operations
    if choice=="1":
        amount = int(input("Enter the amount to deposit: "))
        b.deposit(amount)
    elif choice=="2":
        amount = int(input("Enter the amount to withdraw: "))
        b.withdraw(amount)
    elif choice=="3":
        b.check_balance()
    elif choice=="4":
        b.show_details()
    elif choice=="5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")

