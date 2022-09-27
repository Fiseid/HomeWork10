def oops():
    raise IndexError


def oops_2():
    try:
        oops()
    except IndexError:
        print("something wrong")


oops_2()
oops()