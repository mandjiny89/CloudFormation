##### Basic if statement

 a = 10
if a ==10:
    print("wow")
else:
    print("sad")

##### let's use if with some manual input value using input function

a = input("Enter your message to world \n>").lower()
if a== "ada rama":
    print("edu serupa")
elif a== "jai sri ram":
    print("jayam undagatam")
elif a== "kadavula":
    print("pozavhi poo")
else:
    print("sethu poo naya")

##### Lets get introduced to the multiple IF statement

a = "true"

if a == "true":
#if a == "not true":
#  if we enable this line it will trigger the else condition which is assocated with first if.
#  As we got true in the first if statment the job will be passed to the next if condtion with in the function.

    print("\n First sammy kumbuda poo\n")
    sammy = input(" sammy asking uneaku yenna vennum\n>")

    sammy=sammy.lower()
    if sammy =="laddu vennum":
        print("sethu poo naya")
    elif sammy=="ellam nalla irukanum":
        print("intha laddu")
    else:
        print("indru poi nalli va")
else:
    print("uneaku laddu kediyathu")
