class Account:
    apr =3.0
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = 'Generic Account'

    @property
    def account_number(self):
       return self._account_number
       
    @account_number.setter
    def account_number(self,value):
        if len(str(value)) != 5:
            raise ValueError('account number shall be 5 chars')
        else:
            self._account_number = str(value)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value <= 0:
            raise ValueError('Balance must be greater tha ZERO')
        else:
          self._balance = value

    def calc_interest(self):
        return f'Cal interest on {self.account_type} with APR = {self.__class__.apr}'


    def __repr__(self):
        return f"""-->     Account
    apr: {self.__class__.apr}
    number: {self.account_number}
    balance: ${self.balance}
    account type: {self.account_type}"""+ '\n' 


class Savings(Account):
    apr = 5.0
    
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)
        self.account_type = 'Saving'



if __name__ == "__main__":
    a = Account(12345, 200)
    print(a)
    print(f'Account a interest APR is {a.calc_interest()}')
    s = Savings(67890, 1000)
    print(s)
    print(f'Savings s interest APR is {s.calc_interest()}')
