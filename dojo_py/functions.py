# Functions are collection of code or instructions

def func_name():
    # collection of code goes here
    print("This is just a demo of what I can do")

    # The above collection has no effect unless when called


# to call call (use) the function, we just have totype the name of the function followed by parenthesis

func_name()  # eg

# you can use a function as many times as possible

func_name()
func_name()

# Fuctions can be used in mapping


def func_map(x):  # here we added a parameter
    # parameters are was we create rooms for arguments to be passed into our function

    return (3+x)  # we mapped the "x to this statement"

# Now when calling the function, we must pass in arguments


x = int(input("Enter any numeric value: "))
# we called the function and passed the input to the function then store the return value from the mapping into 'y'

d = func_map(x)

print(d)  # Here we print d


# Its also possible to have more than one arguments in a function

def func_more_args(x, y):
    return x+y


c = func_more_args(5, 7)
print(c)


name1 = "Victor"
height1 = 2.7
weight1 = 89


name2 = "Inem"
height2 = 2.2
weight2 = 98

name3 = "Christy"
height3 = 2
weight3 = 70


# BMI with functions
def bmi_calc(name, weignt, height):
    bmi = (weignt/(height ** 2))
    if bmi <= 25:
        return (f"{name} is not overweight")
    else:
        return (f"{name} is overweight")


result1 = bmi_calc(name1, height1, weight1)
result2 = bmi_calc(name2, height2, weight2)
result3 = bmi_calc(name3, height3, weight3)

print(result1)
print(result2)
print(result3)
