from __future__ import annotations
from abc import ABC, abstractmethod

class Product(ABC):
    
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):

    def operation(self) -> str:
        return "Result of the ConcreteProductA"

class ConcreteProductB(Product):

    def operation(self) -> str:
        return "Result of the ConcreteProductB"

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = product.operation()
        return result

class ConcreteCreatorA(Creator):

    def factory_method(self) -> ConcreteProductA:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):

    def factory_method(self) -> ConcreteProductA:
        return ConcreteProductB()

def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    client_code(ConcreteCreatorA())
