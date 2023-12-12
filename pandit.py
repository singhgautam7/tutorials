name = "Python Pandit"
place = "Bharat"
age = 26

def how_to_use():
    # Instead of this
    print("My name is " + name)

    # Do this for the same output
    print(f"My name is {name}")

    # i.e. we add letter 'f' before defining a string
    #  and we add curly braces to embed python code

def easy_print_variables():
    # Instead of this
    print(f"name = {name}")
    print(f"place = {place}")
    print(f"age = {age}")

    # Do this for the same output
    print(f"{name = }")
    print(f"{place = }")
    print(f"{age = }")

    # i.e. just adding '=' after variable name inside
    # curly braces will print the variable name with
    # the value

def arithmetic_and_conversion():
    # Arithmetic operation
    num1 = 80
    num2 = 20
    print(f"The sum is{num1 + num2}")

    # Limiting decimal digits
    pi = 22/7
    print(f"{pi = }")
    print(f"pi with 2 decimals = {pi:.2f}")    # .2f = only 2 decimal digits

    # Converting to binary
    print(f"My age = {age}")
    print(f"My age in binary = {age:b}")    # b = binary. similar can be done for octal and hexadecimal

    # Comma separated integer
    not_my_money = 123456789
    print(f"{not_my_money = :0,}")

def datetime_to_string():
    from datetime import datetime

    now = datetime.now()

    # Instead of this
    formatted_date_1 = now.strftime("%Y-%b-%d %H:%M:%S")
    print(f"{formatted_date_1 = }")

    # you can try this
    formatted_date_2 = f"{now:%Y-%b-%d %H:%M:%S}"
    print(f"{formatted_date_2 = }")

def other_methods_of_str_format():
    # Using str.format()
    print("My name is {f_name}, I am {f_age}".format(f_name = name, f_age = age))
    print("My name is {0}, I am {1}".format("Python Pandit", 26))

    # Using % operator
    print("My name is %s, I am %d" % (name, age))   # %s means string variable and %d means int variable


def speed_comparison():
    import timeit

    string1 = "My name is {f_name}, I am {f_age}".format(f_name=name, f_age=age)
    string2 = "My name is %s, I am %d" % (name, age)
    string3 = f"My name is {name}, I am {age}"

    print(f"{string1 = }")
    print(f"{string2 = }")
    print(f"{string3 = }")

    method1 = lambda: string1
    method2 = lambda: string2
    method3 = lambda: string3

    time1 = timeit.timeit(method1, number=100000)
    time2 = timeit.timeit(method2, number=100000)
    time3 = timeit.timeit(method3, number=100000)

    print(f"Avg time taken by str.format() = {time1}")
    print(f"Avg time taken by % operator = {time2}")
    print(f"Avg time taken by f-strings = {time3}")


if __name__ == '__main__':
    speed_comparison()