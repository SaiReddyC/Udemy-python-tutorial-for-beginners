from abc import ABC, abstractmethod


class AbstractRecipe(ABC):

    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def recipe(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Recipe1(AbstractRecipe):

    def prepare(self):
        print("do the dishes")
        print("get raw materials")

    def recipe(self):
        print("execute the steps")

    def cleanup(self):
        print("Cleaning up")


class Microwave(AbstractRecipe):

    def prepare(self):
        print("do the dishes")
        print("get raw materials")
        print("switch on microwave")

    def recipe(self):
        print("execute the steps")

    def cleanup(self):
        print("Cleaning up")
        print("switch off microwave")


Recipe1().execute()
Microwave().execute()
