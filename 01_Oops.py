l = [1,2,3]
print(type(l))

class Atm:
    #constructor
    def __init__(self):
        self.balance = 0
        self.pin = ''
        self.reg_mobile = 1234567890
        # self.main_page()
        print(id(self))

    def main_page(self):
        user_entry = input(""" 
        Welcome to the ATM Machine:
        1. Create pin
        2. Change pin
        3. Check balance
        4. Withdraw cash
        5. Any other number to Exit
        """) 
        
        if user_entry == '1':
            self.Create_pin()

        elif user_entry == '2':
            self.Change_pin()

        elif user_entry == '3':
            self.Check_balance()

        elif user_entry == '4':
            self.Withdraw_cash()
        
        else:
            exit()                    

    def Create_pin(self):
        user_pin = int(input("Enter your pin number:"))
        self.pin = user_pin

        user_balance = int(input("Enter your balance:"))
        self.balance = user_balance

        print("Pin created successfully")
        self.main_page()

    def Change_pin(self):
        old_pin = int(input("Enter your old pin:"))
        if old_pin == self.pin:
            new_pin = input("Enter your new pin:")
            self.pin = new_pin
            print("Pin change successfully")
            self.main_page()
        else:
            print("Wrong pin")
            self.main_page()

    def Check_balance(self):
        user_pin = int(input("Enter your pin:"))
        if self.pin == user_pin:
            print("Your balance is :",self.balance)
        else:
            print("Wrong pin")
            
        self.main_page()
    
    def Withdraw_cash(self):
        user_pin = int(input("Enter your pin:"))
        if self.pin == user_pin:
            withdraw_amount = int(input("Enter withdraw amount:"))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print("Please collect your cash")
                print("Your remaining balance is :",self.balance)
                self.main_page()
            else:
                print("Insufficient balance")
        else:
            print("Wrong pin")
            
        self.main_page()


obj = Atm()
print(id(obj))
# obj.Change_pin()

# print(type(obj))

#Creating our own data type
class Fraction:

    def __init__(self, x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
    
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.num * other.den
        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.num * other.den 
        new_den = self.den * other.num
        return '{}/{}'.format(new_num, new_den)
    
f1 = Fraction(4,2)
print(type(f1))
print(f1)
f2 = Fraction(1,2)
print(f2)
print("add",f1+f2)
print("sub",f1-f2)
print("mul",f1*f2)
print("div",f1/f2)