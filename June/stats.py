from menu import *
from random import randint
from math import sqrt

def intput(query):
    while 1:
        try:
            return int(input(query))
        except:
            query = "Please enter an integer: "

menu = Menu()

nums = []

@menu.add("Add Number")
def a():
    nums.append(intput("Number to add: "))

@menu.add("Remove Number")
def a():
    i = intput("Number to remove: ")
    if not i in nums:
        print(f"{i} is not in the list")
        return
    nums.remove(i)

@menu.add("Remove Index")
def a():
    i = intput("Index to remove at: ")
    if i < 0 or i >= len(nums):
        print(f"{i} is out of range")
        return;
    nums.pop(i)

@menu.add("Show List")
def a():
    print(nums)

def mean(l):
    return sum(l)/len(l)
@menu.add("Compute Mean")
def a():
    print(f"Mean of list is {mean(nums)}")

def median(l):
    l = l.copy()
    l.sort()
    c = len(l)
    mid = c//2
    if c % 2:
        return l[mid]
    else:
        return (l[mid] + l[mid-1])/2
@menu.add("Compute Median")
def a():
    print(f"Median of list is {median(nums)}")

def midpoint(l):
    return (max(l)+min(l)) / 2
@menu.add("Compute Midpoint")
def a():
    print(f"Midpoint of list is {midpoint(nums)}")

def mode(l):
    counts = {}
    for n in l:
        if not n in counts:
            counts[n] = 0
        counts[n] += 1
    m = max(counts.values())
    modes = []
    for c, v in counts.items():
        if v == m:
            modes.append(c)
    return modes
@menu.add("Compute Mode(s)")
def a():
    print(f"Modes of list are {mode(nums)}")

def stddev(l):
    lmean = mean(l)
    return sqrt(sum([(n - lmean) ** 2 for n in l])/len(l))
@menu.add("Compute Standard Deviation")
def a():
    print(f"Standard Deviation of list is {stddev(nums)}")

'''
@menu.add("Add random int")
def a():
    i = randint(0, 100)
    nums.append(i)
    print(f"Added {i} to the list")
#'''

while menu.prompt(): pass

