import random
from beverages import *


class CoffeeMachine:
    def __init__(self):
        self.served = 0

    class EmptyCup(HotBeverage):
        price = 0.90
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, msg="This coffee machine has to be repaired."):
            super().__init__(self, msg)

    def repair(self):
        self.served = 0
        print("This machine is repaired")

    def serve(self, param):
        empty = self.EmptyCup()
        self.served += 1
        if self.served > 9:
            raise self.BrokenMachineException()

        r = random.randint(1, 2)
        ret = param
        if r == 1:
            ret = self.EmptyCup()
        return ret


def test_coffee_machine():
    cafe = Coffee()
    print(cafe)
    choc = Chocolate()
    print(choc)
    cappuc = Cappuccino()
    print(cappuc)
    tea = Tea()
    print(tea)
    machine = CoffeeMachine()
    for i in range(30):
        try:
            a = machine.serve(cafe)
            print(a)
        except machine.BrokenMachineException as e:
            print(e)
            machine.repair()


if __name__ == '__main__':
    test_coffee_machine()
