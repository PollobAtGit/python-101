
def decorator_to_any_func(fn):
    
    if not fn:
        print("function is not defined")
    else:
        def other_func():
            try:
                alert_to_print = "i am alerting you"
                fn(alert_to_print)
            except Exception as e:
                print("exception occurred")
            finally:
                print("cleaning everything")

        return other_func



# once a function has been decorated it will always be wrapped with the decorator
@decorator_to_any_func
def print_message(msg):
    print(msg)

print(type(decorator_to_any_func(print_message)))

print_message()


def calculate_timing(fn):

    if not fn:
        print("function is not defined")
    else:
    
        def wrapper(n):

            import time

            start_time = time.time()

            total_sum = fn(n)

            end_time = time.time()

            print("time taken to execute the function : " + str((end_time - start_time)))

            return total_sum

        return wrapper

@calculate_timing
def iterate_to_n(n):
    
    if n:

        total_sum = 0
        for x in range(1, n + 1):
            total_sum = total_sum + x

        return total_sum


print((iterate_to_n(100999)))


# print(calculate_timing(iterate_to_n)(10000000))

