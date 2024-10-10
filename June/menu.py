import math
import random

def menuOption(menu, name):
    return lambda func : menu.addOption(name, func)


class Menu:

    def __init__(self):
        self.options = []

    def addOption(self, name, func):
        self.options += [(name, func)]

    def add(self, name):
        return lambda func : self.options.append((name, func))

    def prompt(self):
        print("[2J[H", end="")
        i = 1
        for (name, _) in self.options:
            print(f"{i}:	{name}")
            i += 1
        print(f"0:	Quit")
        inp = int(input(">> "))
        if inp > 0 and inp <= len(self.options):
            self.options[inp - 1][1]()
            input("-- Press enter to continue --")
            return True
        else:
            return False

def isPrime(x):
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


