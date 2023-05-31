# # Working on loops to grasp the idea

# my_list = ["banana", "apple", "microsoft"]

# for var_name in my_list:
#     print(var_name)


# # Printing each characters with while loop
# statement = "Choco"
# indx = 1
# while indx <= 4:

#     print(indx, statement[indx])  # I'm also printing the index
#     indx += 1  # This will increament the value of indx until it gets to 5 thereby satisfying the statement


# # Another loop practice addition of elements

# items_ = [10, 7, 2, 3]
# sum = 0
# for elements in items_:
#     sum = sum+elements
#     print(elements)
#     print(sum)


# #  Using range

# for i in range(1, 12, 2):
#     print(i)


# total3 = 0
# for new_ in range(1, 8):
#     if (new_ % 3) == 0:
#         total3 += new_
#        # print(total3)
# print(total3)

# sumcomp = 0
# for comp_ in range(1, 100):
#     if (comp_ % 3) == 0:
#         sumcomp += comp_
#         if (comp_ % 5) == 0:
#             sumcomp += comp_
# print(sumcomp)


# given_list = [5, 4, 4, 3, 1, -1, -2, -3]
# sum_pos_list = 0
# items_ = 0
# while items_ < len(given_list) and given_list[items_] > 0:
#     sum_pos_list += given_list[items_]
#     items_ += 1

# print(sum_pos_list)

# given_list = [5, 4, 4, 3, 1, -1, -2, -3]

# sum_ = 0
# for items_ in given_list:
#     if items_ <= 0:
#         break
#     sum_ += items_
#     items_ += 1
# print(sum_)


# given_list = [5, 4, 4, 3, 1, -1, -2, -3]
# sum_ = 0

# i = 0
# while given_list[i] >= 0:
#     sum_ += given_list[i]

#     print(i, end="")
#     print("")
#     i += 1
# print(sum_)


# colourlist = ["green", "yellow", "red"]
# for i in colourlist:
#     print(i)


# given_list = [7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7]
# sum_ = 0


# for i in given_list:
#     if i <= 0:
#         sum_ += i
# print(sum_)


given_list = [7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7]
sum_ = 0
i = 0

while i in range(len(given_list)):
    if given_list[i] < 0:
        sum_ += given_list[i]
    i += 1

print(sum_)
