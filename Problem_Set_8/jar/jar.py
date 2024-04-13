import sys

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size
    
    def deposit(self, n):
        if type(n) != int:
            raise ValueError("Not an integer!")
        elif self.size + n > self.capacity:
            raise ValueError("No capacity!")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if type(n) != int:
            raise ValueError("Not an integer!")
        elif self.size - n < 0:
            raise ValueError("Not enough coockies in the jar!")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int:
            raise ValueError("Not an integer!")
        elif capacity < 0:
            raise ValueError("Capacity is a non-negative integer!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise ValueError("Not an integer!")
        elif size > self.capacity:
            raise ValueError("Low capicity!")
        self._size = size
    
    @classmethod
    def get(cls):
        try:
            capacity = int(input("Capacity: "))
            size= int(input("Size: "))
            return cls(capacity, size)
        except:
            raise ValueError("Not an integer!")

def main():
    jar = Jar.get()
    while True:
        try:
            jar.deposit(int(input("Add: ")))
            jar.withdraw(int(input("Withdraw: ")))
            print(jar)
        except KeyboardInterrupt:
            sys.exit("End of coockies!")


if __name__ == "__main__":
    main()