import math

globalList = []
exitVal = 1

def printMenu():
    print("1 - Append Item to List")
    print("2 - Delete Item by Item Value")
    print("3 - Delete Item by Index")
    print("4 - Print List")
    print("5 - Find Mean")
    print("6 - Find Median")
    print("7 - Find Midpoint")
    print("8 - Find Mode(s)")
    print("9 - Compute Standard Division")
    print("0 - Exit")

def takeInput(userInput):
    global exitVal
    if userInput == 1:
        appendItem(float(input("What would you like to append?")))
    elif userInput == 2:
        deleteByValue(float(input("Please input your value:")))
    elif userInput == 3:
        deleteByIndex(int(input("Please enter your index:")))
    elif userInput == 4:
        printList()
    elif userInput == 5:
        findMean()
    elif userInput == 6:
        findMedian()
    elif userInput == 7:
        findMidpoint()
    elif userInput == 8:
        findMode()
    elif userInput == 9:
        computeDeviation()
    elif userInput == 0:
        exitVal = 0
        print("Exit placeholder")
    else:
        print("Invalid Input Receieved")

def appendItem(appendee):
    globalList.append(appendee)

def deleteByValue(value):
    while value in globalList:
        globalList.remove(value)

def deleteByIndex(index):
    globalList.pop(index)

def printList():
    print(', '.join(map(str, globalList)))

def findMean():
    total = 0
    for x in range (0, len(globalList)):
        total = globalList[x] + total
    return(total / len(globalList))


def findMedian():
    temp = globalList.copy()
    temp.sort()
    if len(globalList) % 2 == 0:
        middle = temp[int(len(temp) / 2)]
        midAdd = temp[int((len(temp) / 2) - 1)]
        print((middle + midAdd) / 2)
    else:
        print(temp[int(len(temp) / 2)])

def findMidpoint():
    if len(globalList) % 2 == 0:
        middle = globalList[int(len(globalList) / 2)]
        midAdd = globalList[int((len(globalList) / 2) - 1)]
        print((middle + midAdd)/ 2)
    else:
        print(globalList[int(len(globalList) / 2)])

def findMode():
    sortedList = globalList
    sortedList.sort()
    numberDict = {}
    for x in range (0, len(sortedList)):
        if not sortedList[x] in numberDict:
            numberDict[sortedList[x]] = 1
        else:
            numberDict[sortedList[x]] += 1

    print(max(zip(numberDict.values(), numberDict.keys()))[1])

def computeDeviation():
    mean = findMean()
    tempList = []
    total = 0
    for x in range (0, len(globalList)):
        tempList.append((globalList[x] - mean) * (globalList[x] - mean))
    for y in range (0, len(tempList)):
        total = total + tempList[y]
    total = total / (len(tempList) - 1)
    print(math.sqrt(total))



printMenu()

while exitVal != 0:
    takeInput(int(input("Input your value")))





