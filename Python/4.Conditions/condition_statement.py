correct = int(input("Enter your guess number"))
if correct == 100:
    print("Perfect")
elif correct < 100:
    print("too less")
elif correct > 100:
    print("too high")
