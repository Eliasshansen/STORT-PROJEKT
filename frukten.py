import random

Fruits = ("apple", "banana", "orange")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + Fruits[fnr-1] + "cums here \n")

while looping: 
    go = input("vill du välja en frukt till? j/n")
    print("\n")

    if (go == "n"):
        break
