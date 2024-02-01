import time

def calculate_time(function):
    def inner():
        begin = time.time()
        function()
        end = time.time()
        print(f"Total runtime of {function.__name__} = {end - begin}")
    return inner

@calculate_time
def my_func_1():
    time.sleep(1)

@calculate_time
def my_func_2():
    time.sleep(2)

if __name__ == '__main__':
    my_func_1()
    my_func_2()
