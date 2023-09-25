class bank:
    def __init__(self):
        self.accounts = {}
    def create(self,acc_no,initial_bal=0.0):
        if acc_no not in self.accounts:
            self.accounts[acc_no] = initial_bal
            return "Account created"
        else:
            return "Account already present"
    def bal(self, acc_no):
        if acc_no in self.accounts:
            return f"Bal of {acc_no}: ${self.accounts[acc_no]:.2f}"
        else:
            return "Account no. doesn't exist"
    def deposit(Self,acc_no, amount):
        if acc_no in self.accounts():
            if amount >0:
                self.accounts[acc_no] += amount
                return f"Dep ${amount:.2f} in {acc_no}. New BAL: ${self.accounts[acc_no]:.2f}"
            else:
                return "no change in amount"
        else:
            return f"{acc_no} nonexistent"

bank=bank()
print(bank.create("1",1000.0))
print(bank.create("2"))

print(bank.bal("1"))
print(bank.bal("2"))

