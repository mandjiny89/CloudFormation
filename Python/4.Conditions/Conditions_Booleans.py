# Conditions are used to check whether the condition is true or fales.
# Boolean is either 0 or 1, 1 means true, 0 means false

# This is a very basic condtion

a = 100
b = 10
c = a==b
d = a!=b
e = a < b
f = a > b
print(c, d, e, f)



# This is using multiple conditions in single line

a = 100
b = 10

c = a==b or a>=b
d = a==b and a<=b
print(c,d)