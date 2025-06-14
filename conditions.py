name = input("please enter your name: ")

age = int(input("please enter your age: "))


if name == "bob":
    print("your name is old so you can come in")
elif age >= 72:
    print("you can enter te club but probably shouldn't")
elif age >= 21:
    print("you can enter the club")
elif age >= 18:
    print("hold on you are not there yet")
elif age >= 16:
    print("nice try")
else:
    print("you cannot enter club")

    