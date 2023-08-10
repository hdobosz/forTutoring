class Point:
    def __init__(self):
        self.color = 'black'
    color = 'red'

obj = Point()

obj.__class__.color = 'blue'
print(obj.color)
print(Point.color)

print(obj.__class__)
print(Point)




# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self):
#         return self._account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print('Go earn some money')
#
#
# account = BankAccount('123456', 10000)
#
# account.__balance = 10
#
# print(account.get_balance())
# print(account.__dict__)
