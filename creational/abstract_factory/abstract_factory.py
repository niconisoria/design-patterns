from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()
    
    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()
    
    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

class AbstractProductA(ABC):

    @abstractmethod
    def operation_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):

    def operation_a(self) -> str:
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):

    def operation_a(self) -> str:
        return "The result of the product A2."

class AbstractProductB(ABC):

    @abstractmethod
    def operation_b(self) -> str:
        pass

    @abstractmethod
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        pass

class ConcreteProductB1(AbstractProductB):

    def operation_b(self) -> str:
        return "The result of the product B1."
    
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.operation_a()
        return f"The result of the B1 collaborating with the ({result})"

class ConcreteProductB2(AbstractProductB):

    def operation_b(self) -> str:
        return "The result of the product B2."
    
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.operation_a()
        return f"The result of the BB collaborating with the ({result})"

def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_b.operation_b())
    print(product_b.another_operation_b(product_a), end="\n")

if __name__ == "__main__":
    client_code(ConcreteFactory1())