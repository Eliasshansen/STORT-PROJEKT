import random

Frukter = ("apple", "banana", "orange")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + Frukter[fnr-1] + "cums here \n")

while looping: 

    print("-------------------------------------------------")
    print("\nfruitmachine\n")

    i=1

    for Frukt in Frukter:
        print(str(i) + ": " + Frukt)
    i+=1

    Fruktnr = input ("vilken frukt")

    print_fruit(Fruktnr)



    go = input("vill du välja en frukt till? j/n")
    print("\n")

    if (go == "n"):
        break

    print ("------------------------------")
    print("anothaone")
    slumpfrukt = random.randint(1, 3)
    print_fruit(slumpfrukt)


