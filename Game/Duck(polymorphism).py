class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee this is fun")
        elif self.ratio == 1:
            print("This a hard work , but i am flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def swim(self):
        print("come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, Waddle, I Waddle too")

    def swim(self):
        print("come on it, but it is bit cold")

    def quack(self):
        print("Are you penguin?")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()
    # test_duck(percy)
