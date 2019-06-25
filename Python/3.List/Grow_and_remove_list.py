# we can add values in the existing list either single object or multiple object using extend

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable.append("appended variables")

print(["this is append result"], list_variable)



# we can also add multiple objects in the list using extend object value

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable.extend(["1st exteneded value", " 2nd extended value", " 3rd extended value"])

print(["this is extend result"], list_variable)



# this is to find the length of the list we can use len function.

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable.append("appended variables")

print(len(list_variable))



# we can also use replace function to remove certain object from the list and add our new value.


list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable[-1]=("lets remove last value and add next text")

print((["this replace function"], list_variable))


# we can also use insert a new function to certain object from the list anywhere we like using number position.

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable.insert(-1, " we are inserting this new value in -1 location")

print((["this is insert function"], list_variable))


# we can use del fucntion to delete certain object from the list

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

del list_variable[-1]

print(["this is del function"], list_variable)


# we can use remove function to remove certain object from the list.
# make sure you use space if you used in object variable to remove else it will show error
# it will remove only one item at a time

list_variable = ["first variable", " second variable", " third variable", " fourth variable"]

list_variable.remove(" fourth variable")
#list_variable.remove("fourth variable")

print(["this is remove function"], list_variable)
