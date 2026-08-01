# Name: Arsh Patle
# Program: Configurable Payment Processing System Using Strategy Pattern
# Example: SBI Bank

from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class UPI(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using SBI UPI.")


# Concrete Strategy 2
class DebitCard(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using SBI Debit Card.")


# Concrete Strategy 3
class NetBanking(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} successful using SBI Net Banking.")


# Context Class
class PaymentProcessor:

    def __init__(self):
        self.strategy = None

    def set_payment_method(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


# Main Program
processor = PaymentProcessor()

print("===== SBI BANK PAYMENT SYSTEM =====")
print("1. UPI")
print("2. Debit Card")
print("3. Net Banking")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: ₹"))

if choice == 1:
    processor.set_payment_method(UPI())

elif choice == 2:
    processor.set_payment_method(DebitCard())

elif choice == 3:
    processor.set_payment_method(NetBanking())

else:
    print("Invalid Choice")
    exit()

processor.process_payment(amount)
