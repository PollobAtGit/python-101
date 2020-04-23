import time


def show_default_time(time=time.ctime()):
    print(time)


def add_spam_v3(menu=[]):
    menu = [2]
    print(len(menu))


def add_spam_v2(menu=[]):
    menu.append(5)
    print(len(menu))


def add_spam(menu=None):
    if menu is None:
        menu = []

    menu.append('spam')
    return menu


def default_argument_problem():
    lunch = ['baked beans']
    breakfast = ['bacon', 'egg']

    # following will not trigger default argumenet issue as value has been passed
    print(add_spam(lunch))
    print(add_spam(breakfast))

    # default argument will be evaluated
    print(add_spam())
    print(add_spam())


if __name__ == "__main__":
    show_default_time()
    show_default_time()
    show_default_time()

    default_argument_problem()

    add_spam_v2()
    add_spam_v2()

    add_spam_v3()
    add_spam_v3()
