from abc import ABC, abstractmethod


class AbsctAnimal(ABC):
    @abstractmethod
    def bark(self): pass


class Dog(AbsctAnimal):
    def bark(self):
        print("Bow Bow")


print(Dog().bark())
