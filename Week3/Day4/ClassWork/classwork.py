class BankAccount :
    def __init__(self, account_number) :
        self.account_number = account_number
        self.amount = 1000

    def withdraw (self, amount_to_withdraw):
        try:
            if amount_to_withdraw > self.amount :
                raise ValueError("Not enogh money")
            else:
                print("NO PROBLEM TO WITHDRAW")
                self.amount = amount_to_withdraw
        except ValueError as err:
            print("AN ERROR HAPPENED WITH THE AMOUNT")
            self.withdraw(int(input("How much to withdraw")))
    
