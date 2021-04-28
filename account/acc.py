class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """THIS IS A CHECKING ACCOUNT"""
    type = "checking"

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance-amount - self.fee


checking = Checking("account\\balance.txt", 2)
checking.transfer(20)
print(checking.balance)
checking.commit()
print(checking.__doc__)