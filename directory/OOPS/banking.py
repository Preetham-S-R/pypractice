class bank_account():

    interest_rate = 0.04                      # classw variable

    def __init__(self, Name, Balance=0):
        self.name = Name
        self.balance = Balance
        self.transactions = []
        self.transactions.append(f'Account holder :  {self.name}')
        self.transactions.append(f'XXX Initial Amount Deposited {Balance} XXX')

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Deposite madbeko mangya, withdraw alla')
        self.balance = self.balance + amount
        self.transactions.append(f'Amount deposited {amount}')

    def withdrawn(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.transactions.append(f'Amount withdrawn {amount}')
            print(f'please collect the cash {amount}!')
        else:
            raise ValueError('you are Broke')

    def account_transfer(self, to_account, amount):
        if amount > self.balance:
            raise ValueError(f'Abbe {self.name}, kud ke pas paisaa nai hai, Duniyako ko bhatne jaraha hai Bhavla !')
        else:
            to_account.balance += amount
            self.balance -= amount
            self.transactions.append(f'You transferred {amount} to {to_account.name} account')
            to_account.transactions.append(f'{self.name} transferred {amount} to your account')

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print('X' * 10)
        print(f'Balance amount {self.balance}')

    def rate_of_interest(self):
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance += interest_amount
        self.transactions.append(f'interest amount {interest_amount}')


c1 = bank_account('Preetham S R', 2000)
c2 = bank_account('Sharath', 5000)
c3 = bank_account('Sandeep', 10000)
c4 = bank_account('Jayashree', 10001)
c5 = bank_account('Sunil', 45212)
c6 = bank_account('Saurabh', 50000)

# c4.account_transfer(c1, 101)
# c4.statement()
# c1.statement()
# c6.deposit(-200)


class sb_account(bank_account):

    interest_rate = 0.05

    def withdrawn(self, amount):
        if amount >= 10000:
            raise ValueError('cannot withdraw more than 10k')
        super().withdrawn(amount)


sb1 = sb_account('Preetham S R', 20000)
# sb1.withdrawn(1200)
# sb1.rate_of_interest()
# sb1.statement()


class salary_account(bank_account):

    def __init__(self, name):
        self.first_month_salary = True
        self.max_draft_amount = 10000
        self.draft_amount = 0.00
        super(salary_account, self).__init__(name)

    def deposit(self, amount):
        if self.first_month_salary:
            self.first_month_salary = False
            super().deposit(amount + 1000)
        else:
            super(salary_account, self).deposit(amount)

    def overdraft(self, amount):
        if amount + self.draft_amount <= self.max_draft_amount:
            self.balance += amount
            self.draft_amount += amount
            self.transactions.append(f'draft amount deposit {amount}')
        else:
            raise Exception(f'amount exceeding max draft amount {self.max_draft_amount}')


sa1 = salary_account('Preetham S R')
# sa1.deposit(30000)
# sa1.deposit(30000)
# sa1.overdraft(1000)
# sa1.statement()


class senior_account(bank_account):

    interest_rate = 0.9

    def withdrawn(self, amount):
        if amount > 20000:
            raise ValueError('cannot withdraw more than 20k')
        super().withdrawn(amount)


sc1 = senior_account('Jayashree', 100010)
# sc1.withdrawn(20000)
# sc1.statement()


class penalty:
    penalty_amount = 0

    def withdrawn(self, amount):
        self.balance -= 200
        super().withdrawn(amount)
        self.transactions.append(f'transaction charges {self.__class__.penalty_amount}')


class pension_account(penalty, bank_account):
    penalty_amount = 200


pa1 = pension_account('Jayashree', 10001)
pa1.withdrawn(1000)
print(pa1.__dict__)