import time


# default argument 'now' is bound with the value when the statement is created. This is evaluated once only when the
# module is create and function is defined. So after creation of current_time(...) value of 'now' will not be changed
# even if the method is invoked multiple time because 'now' is bound with the value of (time.ctime()) when the function
# was created

# above is a basic issue with any default function argument whose data type is an mutable type because the value might
# change later

def current_time(now=time.ctime()):
    print('now', now)


def proper_current_time():
    print('now', time.ctime())


current_time()
time.sleep(1)

current_time()
time.sleep(1)

current_time()
time.sleep(1)

current_time()
time.sleep(1)

print('done with default argument version with ...ctime()')

proper_current_time()
time.sleep(1)

proper_current_time()
time.sleep(1)

proper_current_time()
time.sleep(1)

proper_current_time()
time.sleep(1)
