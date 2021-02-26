class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.Name = name
        self.Price = price

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        str1 = "name : {} \n".format(self.Name)
        str2 = "price : " + '.%.2f' % self.Price + '\n'
        str3 = self.description() + "\n"
        return str1 + str2 + str3


class Coffee(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.40, "coffe")

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.30, "tea")


class Chocolate(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.50, "chocolate")

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.45, "cappucino")

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


def test():
    hot_beverage = HotBeverage()
    print(hot_beverage)
    cafe = Coffee()
    print(cafe)
    choc = Chocolate()
    print(choc)
    cappuc = Cappuccino()
    print(cappuc)
    tea = Tea()
    print(tea)


if __name__ == '__main__':
    test()
