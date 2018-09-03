def point_compare(a, b):
    if is_point(a) and is_point(b):
        return a[0] - b[0] or a[1] - b[1]


def is_point(p):
    """check if p ls a list of 2"""
    return isinstance(p, (list, tuple)) and len(p) == 2


class Strut(list):
    def __init__(self, ite=[]):
        self.index = 0
        list.__init__(self, ite)


def is_infinit(n):
    return abs(n) == float("inf")


E = 1e-6


def mysterious_line_test(a, b):
    for arg in (a, b):
        if not isinstance(arg, list):
            return True
    return a == b
