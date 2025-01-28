# Task 1: Class with getString and printString methods
class MyString:
    def init(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


# Task 2: Shape and Square classes with area methods
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def init(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Task 3: Rectangle class inheriting from Shape
class Rectangle(Shape):
    def init(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Task 4: Point class with methods for coordinates, moving, and distance
import math

class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# Task 5: Bank Account class
class Account:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} made. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. Remaining balance: {self.balance}")


# Task 6: Filtering prime numbers using filter and lambda
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True