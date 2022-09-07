from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):

    def basicinfo(self):
        print(f"This is a generic bank")
        return "Generic bank: 0"


    @abstractmethod
    def withdraw(self, amount):
        pass


class Swiss(Bank):
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print(f"This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"


    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New balance: {self.bal}")
            return self.bal


def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)


if __name__ == "__main__":
    main()