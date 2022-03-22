class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def check(self, other_user, money):
        if not other_user.checking_account or other_user.balance < money:
            raise ValueError()
        self.balance += money
        other_user.balance -= money
        return self.name + " has " + str(self.balance) + " and " + other_user.name + " has " + str(other_user.balance) + "."

    def withdraw(self, draw):
        if self.balance < draw:
            raise ValueError
        else:
            self.balance -= draw
            return self.name + " has " + str(self.balance) + '.'

    def add_cash(self, money):
        self.balance += money
        return self.name + " has " + str(self.balance) + "."
