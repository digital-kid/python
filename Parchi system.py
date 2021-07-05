import random
print("Parchi system")
print("How many parchis do you have?")
print("2 parchi")
print("3 parchi")
print("4 parchi")
print("5 parchi")
choice=input("2/3/4/5: ")
if choice=='2':
    parchino1=input("Enter the name of first parchi: ")
    parchino2=input("Enter the name of second parchi: ")
    J1=[parchino1,parchino2]
    value = random.choice(J1)
    print(value)
if choice=='3':
    parchino3=input("Enter the name of first parchi: ")
    parchino4=input("Enter the name of second parchi: ")
    parchino5=input("Enter the name of third parchi: ")
    J2=[parchino3,parchino4,parchino5]
    value = random.choice(J2)
    print(value)
if choice=='4':
    parchino6=input("Enter the name of first parchi: ")
    parchino7=input("Enter the name of second parchi: ")
    parchino8=input("Enter the name of third parchi: ")
    parchino9=input("Enter the name of fourth parchi: ")
    J3=[parchino6,parchino7,parchino8,parchino9]
    value = random.choice(J3)
    print(value)
if choice=='5':
    parchino10=input("Enter the name of first parchi: ")
    parchino11=input("Enter the name of second parchi: ")
    parchino12=input("Enter the name of third parchi: ")
    parchino13=input("Enter the name of fourth parchi: ")
    parchino14=input("Enter the name of fifth parchi: ")
    J4=[parchino10,parchino11,parchino12,parchino13,parchino14]
    value = random.choice(J4)
    print(value)
Wait=input(".")

