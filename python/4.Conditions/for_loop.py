# #Basic for loop
#
var = [" 1", " 2", " 3", " 4", " 5", ]

for temporarystorage in var:
    print(" Ticket number", temporarystorage)
print ("\n This is to clear the last memory in temporary_storage", temporarystorage)

# #### another way for loop
#
for temporarystorage in ("1", " 2",):
    print(" Ticket number", temporarystorage)
print ("\n This is to clear the last memory in temporary_storage", temporarystorage)

###Nested loop basic example

#variable = range(2)    # first type
#variable = range(1,4)  # second type
variable = ["I am going", " home", " movie"]
for firstfor in variable:
    for secondfor in variable:
        print(firstfor, secondfor)
print("cleaning last loop variable", firstfor)


#### we can declare the variable in for loop itself these works differently from the above nested loop

for firstfor in [" I love", " I hate",]:
    for secondfor in [" movie", " programming", " Fitness",]:
        print(firstfor, secondfor)

        