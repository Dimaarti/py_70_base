# #1
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class PaymentAliPay(PaymentMethod):
    def __init__(self, number_mobile):
        self.number_mobile = number_mobile

    def pay(self, amount):
        return f"Оплата {amount} бел.руб. с помощью номера телефона {self.number_mobile}"


class PaymentBankPayMethod(PaymentMethod):
    def __init__(self, number_bank_account):
        self.number_bank_account = number_bank_account

    def pay(self, amount):
        return f"Оплата {amount} бел.руб. с номера счета {self.number_bank_account}"


class PaymentCard(PaymentMethod):
    def __init__(self, number_card):
        self.number_card = number_card

    def pay(self, amount):
        return f"Оплата {amount} бел.руб., с карты {self.number_card}"


def payment(payment_method: PaymentMethod, amount: float):
    print(payment_method.pay(amount))
methods = [PaymentAliPay("+3759999111"),
           PaymentBankPayMethod("BY30AKBB301212341234123412341234"),
           PaymentCard("0000 0000 0000 0000")
]


real_amount = 10000.2
print(f"Платеж на сумму {real_amount}")
for method in methods:
    payment(method, real_amount)

# 2
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class SMS(Notification):
    def send(self, message):
        print(f"Отправка SMS: {message}")


class Email(Notification):
    def send(self, message):
        print(f"Отправка Email: {message}")


class MMS(Notification):
    def send(self, picture):
        self.picture = "Вам пришла картинка"
        print(f"Отправка MMS: {self.picture}")


notifications = [SMS(), Email(), MMS()]
for lst_notifications in notifications:
    lst_notifications.send("Вам пришло сообщение")




4

class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3

    def deposit(self, amount: float):
        self.__balance += amount
        if self.__balance >= self.daily_limit:
            print(f"Депозит не возможен, так как превышен лимит в {self.daily_limit}")
        if self.withdrawals_today < self.max_withdrawals:
            self.withdrawals_today += 1
        elif self.withdrawals_today == self.max_withdrawals:
            print("Превышен лимит транзакций")

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Не хватает денег на депозите")

    def get_balance(self):
        return self.__balance


balance = BankAccount()
balance.deposit(200.5)
balance.deposit(300)
balance.deposit(500)
balance.deposit(500)

print(balance.get_balance())
balance.withdraw(1000)
print(balance.get_balance())
