#################################
#    class Account @property    #
#################################


class Account:
    RATE_RUB_TO_USD = 0.013
    RATE_RUB_TO_EUR = 0.011
    SUFFIX_RUB = 'RUB'
    SUFFIX_USD = 'USD'
    SUFFIX_EUR = 'EUR'

    def __init__(self, surname, number, percent, balance=0):
        self.__surname = surname
        self.__number = number
        self.__percent = percent
        self.__balance = balance

        print(f'Счет №{self.number}, принадлежащий {self.surname} был открыт.\n{"*" * 50}')

    def __del__(self):
        print(f'{"*" * 50}\nСчет №{self.number}, принадлежащий {self.surname} был закрыт.')

    @classmethod
    def set_usd(cls, value):
        cls.RATE_RUB_TO_USD = value

    @classmethod
    def set_eur(cls, value):
        cls.RATE_RUB_TO_EUR = value

    @staticmethod
    def convert(value, rate):
        return value * rate

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value):
        self.__percent = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def get_usd(self):
        value = Account.convert(self.balance, self.RATE_RUB_TO_USD)
        return f'Состояние счёта: {value} {self.SUFFIX_USD}'

    def get_eur(self):
        value = Account.convert(self.balance, self.RATE_RUB_TO_EUR)
        return f'Состояние счёта: {value} {self.SUFFIX_EUR}'

    def add_percents(self):
        self.balance += self.balance * self.percent
        print(f'Проценты были успешно начислены!')
        return self.get_balance()

    def withdraw_money(self, value):
        if value > self.balance:
            print(f'Недостаточно средств на счете!')
        else:
            self.balance -= value
            print(f'{value} {self.SUFFIX_RUB} успешно снято.')
        return self.get_balance()

    def add_money(self, value):
        self.balance += value
        print(f'Сумма {value} {self.SUFFIX_RUB} успешно добавлена.')
        return self.get_balance()

    def get_balance(self):
        text = f'Текущий баланс: {self.balance} {self.SUFFIX_RUB}\n{"-" * 20}'
        return text

    def get_info(self):
        text = f'Информация о счете:\n{"-" * 20}\n№{self.number}\nВладелец: {self.surname}' + \
               f'\nТекущий баланс: {self.balance} {self.SUFFIX_RUB}' + \
               f'\nПроценты: {self.percent:.0%}\n{"-" * 20}'
        return text


account = Account('Долгих', 12345, 0.03, 1000)
print(account.get_info())
print(account.get_usd())
print(account.get_eur())

account.surname = 'Сергеев'

Account.set_usd(2)
print(account.get_usd())
print(account.add_percents())
print(account.withdraw_money(400))
print(account.withdraw_money(4000))
print(account.add_money(500))





#######################################
#    class Account set() and get()    #
#######################################


# class Account:
#     RATE_RUB_TO_USD = 0.013
#     RATE_RUB_TO_EUR = 0.011
#     SUFFIX_RUB = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, number, percent, balance=0):
#         self.__surname = surname
#         self.__number = number
#         self.__percent = percent
#         self.__balance = balance
#
#         print(f'Счет №{self.__number}, принадлежащий {self.__surname} был открыт.\n{"*" * 50}')
#
#     def __del__(self):
#         print(f'{"*" * 50}\nСчет №{self.__number}, принадлежащий {self.__surname} был закрыт.')
#
#     @classmethod
#     def set_usd(cls, value):
#         cls.RATE_RUB_TO_USD = value
#
#     @classmethod
#     def set_eur(cls, value):
#         cls.RATE_RUB_TO_EUR = value
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def set_surname(self, value):
#         self.__surname = value
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_number(self, value):
#         self.__number = value
#
#     def get_number(self):
#         return self.__number
#
#     def set_percent(self, value):
#         self.__percent = value
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_balance(self, value):
#         self.__balance = value
#
#     def get_balance(self):
#         return self.__balance
#
#     def get_usd(self):
#         value = Account.convert(self.__balance, self.RATE_RUB_TO_USD)
#         return f'Состояние счёта {self.SUFFIX_USD}: {value} {self.SUFFIX_USD}'
#
#     def get_eur(self):
#         value = Account.convert(self.__balance, self.RATE_RUB_TO_EUR)
#         return f'Состояние счёта {self.SUFFIX_EUR}: {value} {self.SUFFIX_EUR}'
#
#     def add_percents(self):
#         self.__balance += self.__balance * self.__percent
#         print(f'Проценты были успешно начислены!')
#         return self.get_balance()
#
#     def withdraw_money(self, value):
#         if value > self.__balance:
#             print(f'Недостаточно средств на счете!')
#         else:
#             self.__balance -= value
#             print(f'{value} {self.SUFFIX_RUB} успешно снято.')
#         return self.get_balance()
#
#     def add_money(self, value):
#         self.__balance += value
#         print(f'Сумма {value} {self.SUFFIX_RUB} успешно добавлена.')
#         return self.get_balance()
#
#     def get_balance(self):
#         text = f'Текущий баланс: {self.__balance} {self.SUFFIX_RUB}\n{"-" * 20}'
#         return text
#
#     def get_info(self):
#         text = f'Информация о счете:\n{"-" * 20}\n№{self.__number}\nВладелец: {self.__surname}' + \
#                f'\nТекущий баланс: {self.__balance} {self.SUFFIX_RUB}' + \
#                f'\nПроценты: {self.__percent:.0%}\n{"-" * 20}'
#         return text
#
#
# account = Account('Долгих', 12345, 0.03, 1000)
# print(account.get_info())
# print(account.get_usd())
# print(account.get_eur())
#
# account.set_surname('Сергеев')
#
# Account.set_usd(2)
# print(account.get_usd())
# print(account.add_percents())
# print(account.withdraw_money(400))
# print(account.withdraw_money(4000))
# print(account.add_money(500))



