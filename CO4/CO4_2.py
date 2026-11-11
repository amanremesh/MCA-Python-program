class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self):
        amt = float(input("Enter deposit amount: "))
        if amt > 0:
            self.balance += amt
            print("Deposited:", amt)
        else:
            print("Invalid amount")

    def withdraw(self):
        amt = float(input("Enter withdrawal amount: "))
        if 0 < amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    def display(self):
        print("\nAccount No:", self.acc_no)
        print("Name:", self.name)
        print("Type:", self.acc_type)
        print("Balance:", self.balance)


acc = BankAccount( 101, "Aman Remesh ", "Savings", 5000)
acc.display()
acc.deposit()
acc.withdraw()
acc.display()