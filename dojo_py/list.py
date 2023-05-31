# List datatype is used to store a list of things
# It is similar to arrays in C


# Defining a list
a = [1, -7, 6]

print(a)

# Append an item to the list
a.append(1)  # it will add the item "1" to the end of the list.

print(a)

# In Python unlike some other languages, You can have a list of mixed types

a.append("Choco")

print(a)


# You can also create nested lists

a.append(["Marissa", "Ajike", "Njay"])

print(a)


# We can use the pop to delete the last item on the list

a.pop()  # This removes the nested list

print(a)

# to access the first item we can use the index [0]

print(a[0])

# Use [-1] to access the last item

print(a[-1])

# use []:] to slice the list

# This will print the items up to but not including index 4 which is the fifth item
print(a[0:4])


# you can modify the value of an item by;
# list[index] = new_val

a[3] = "Ify"
print(f"{a}")


b = ["banana", "apple", "microsoft"]
tmp = b[0]
b[0] = b[-1]
b[-1] = tmp

print(b)

# Another way to solve the above challenge is;

b[-1], b[0] = b[0], b[-1]

print(b)


# Converting a range to a list

z = list(range(1, 10, 2))  # I used the last parame to skip 2
print(z)
