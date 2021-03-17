import datetime
import pytz

# The mini challenge is to change the class so that the amount used to open the account also appears in the
# transaction list. No change should be made to the main part of the program, only the class can be changed.


class Account:
    """ Simple account class with balance """
    @staticmethod  # do not use self with the methods contained in this function
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), amount))
        else:
            print("The amount must be greater than 0 and not greater than your account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawal"
                amount *= -1
            print("{:6} {} on (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    #  tim.show_balance()
    tim.withdrawal(500)
    tim.withdrawal(50000)
    #  tim.show_balance()

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdrawal(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)




