# It refers to a location in memory where a value is stored.
# In python, variables are like nametags and not a box


# a = 1
# print(a)


# b = 2
# print(b)
# c = ("hello there")
# print(c)


# try thiswith C
# a = 2
# b = a
# a = 3
# print(a)
# print(b)

# Exercise (Swapping values)

v1 = "first string"
v2 = "second string"

print(v1)
print(v2)

# introduce a temp variable...

tmp = v1
v1 = v2
v2 = tmp
del (tmp)
print(v1)
print(v2)
try:
    print(tmp)  # It will throw an error because tmp was deleted
except:
    print("Tmp was deleted")
