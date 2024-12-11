
import statistics
selections = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10

def menu():
    user = 0
    while user != 10:
        printMenu()
        user = int(input("type in the number of your choice "))
        if user == 1:
            menuItemOne()
        if user == 2:
            menuItemTwo()
        if user == 3:
            menuItemThree()
        if user == 4:
            menuItemFour()
        if user == 5:
            menuItemFive()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            menuItem8()
        if user == 9:
            menuItem9()
            print("yes")
        if user == 10:
            print("thank you for using the menu")

def printMenu():
    print("1. Item 1 ")
    print("2. Item 2 ")
    print("3. Item 3 ")
    print("4. Item 4 ")
    print("5. Item 5 ")
    print("6. Item 6 ")
    print("7. Item 7 ")
    print("8. Item 8 ")
    print("9. Item 9 ")
    print("10. exit")

def menuItemOne():
    print("This is Menu Item 1")
    userin = int(input("give me an number "))
    selections.append(userin)
    print(selections)
def menuItemTwo():
    print("This is Menu Item 2")
    print(selections)
    userin2 = int(input("what do you want to remove "))
    selections.remove(userin2)
    print(selections)

def menuItemThree():
    print("This is Menu Item 3")
    print(selections)
    userin3 = int(input("what do you want to remove "))
    selections.pop(userin3)
    print(selections)
def menuItemFour():
    print("This is Menu Item 4")
    print(selections)
def menuItemFive():
    print("This is Menu Item 5")
    print(selections)
    print(statistics.mean(selections))
def menuItemSix():
    print("This is Menu Item 6")
    statistics.median(selections)
    statistics.median(map(float, selections))
    from decimal import Decimal
    statistics.median(map(Decimal, selections))
    print(selections)
def menuItemSeven():
# find some way to make selections have a mid point by the length
    midpoint= int(len(selections)/2)
    for val in selections[:midpoint]:
        print(val)
    print("This is Menu Item 7")
    if selections == 3:
        mid = 3+4
        mid/2
        print(mid)

def menuItem8():
    print("yes8")
def menuItem9():
    print("yes9")

def main():
    menu()

if __name__ == '__main__':
    main()
