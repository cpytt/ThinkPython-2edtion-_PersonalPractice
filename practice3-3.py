# method1
"""
def print_form():
    print1()
    print2()
    print2()
    print2()
    print2()
    print1()
    print2()
    print2()
    print2()
    print2()
    print1()


def print1():
    print('+----+----+')


def print2():
    print('|    |    |')


print_form()
"""


# method2

def do_twice(fun):
    fun()
    fun()


def do_four(fun):
    do_twice(fun)
    do_twice(fun)


def print_beam():
    print('+ - - - - ', end='')


def print_post():
    print('|         ', end='')


# + - - - - + - - - - +
def print_beams():
    do_twice(print_beam)  # 当函数作为参数时，不用加括号
    print('+')


# |         |         |
def print_posts():
    do_twice(print_post)
    print('|')


# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()


# print a 2*2 grid


def test_beam(y):
    i = 1
    while i <= y:
        print_beam()
        i += 1
    print('+')


def test_post(y):
    j = 1
    while j <= 4:
        i = 1
        while i <= y:
            print_post()
            i += 1
        print('|')
        j += 1


def test_row(y):
    test_beam(y)
    test_post(y)


# print x rows,y columns grid
def test_print_grid(x, y):
    i = 1
    while i <= x:
        test_row(y)
        i += 1
    test_beam(y)


test_print_grid(5, 6)
