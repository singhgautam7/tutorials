name = "Python Pandit"
place = "India"
age = 26

def how_to_use():
    # Instead of this
    print("My name is " + name) # not an f-string

    # Do this for same output
    print(f"My name is {name}")

    # i.e. we add letter 'f' before defining a string
    #  and we use curly braces to embed python code

def easy_print_variables():
    # Instead of this
    print(f"name = {name}")
    print(f"place = {place}")
    print(f"age = {age}")

    # Do this for same output
    print(f"{name = }")
    print(f"{place = }")
    print(f"{age = }")

    # i.e. just adding '=' after variable name inside
    #  curly braces will print the variable name with
    #  the value

def arithmetic_and_conversions():
    # Arithmetic operation
    num1 = 80
    num2 = 20
    print(f"The sum is{num1 + num2}")

    # Limiting decimal digits
    pi = 22/7
    print(f"{pi = }")
    print(f"pi with 2 decimals = {pi:.2f}")    # .2f = only 2 decimal digits

    # Converting to binary
    print(f"My age in binary = {age:b}")    # b = binary. similar can be done for octal and hexadecimal

    # Comma separated integer
    not_my_money = 123456789
    print(f"{not_my_money = :,}")


def datetime_to_string():
    from datetime import datetime

    today_date = datetime.now() # Get today's date

    # Instead of this
    formatted_date_1 = today_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{formatted_date_1 = }")

    # You can also try this
    formatted_date_2 = f"{today_date: %Y-%m-%d %H:%M:%S}"
    print(f"{formatted_date_1 = }")

def other_methods_of_str_format():
    # Using str.format()
    print("My name is {f_name}, I am {f_age}".format(f_name = name, f_age = age))
    print("My name is {0}, I am {1}".format("Python Pandit", 26))

    # Using % operator
    print("My name is %s, I am %d" % (name, age))   # %s means string variable and %d means int variable

def speed_comparison():
    import timeit
    name = "Python Pandit"
    place = "India"
    age = 26

    method1 = lambda: "My name is {f_name}, I am {f_age}".format(f_name = name, f_age = age)
    method2 = lambda: "My name is %s, I am %d" % (name, age)
    method3 = lambda: f"My name is {name}, I am {age}"

    time1 = timeit.timeit(method1, number=100000)
    time2 = timeit.timeit(method2, number=100000)
    time3 = timeit.timeit(method3, number=100000)

    print(f"Time taken by str.format() = {time1}")
    print(f"Time taken by % operator = {time2}")
    print(f"Time taken by f-strings = {time3}")


if __name__ == '__main__':
    how_to_use()
    easy_print_variables()
    arithmetic_and_conversions()
    datetime_to_string()
    other_methods_of_str_format()
    speed_comparison()
