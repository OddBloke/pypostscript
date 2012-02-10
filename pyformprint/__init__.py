class AllIntegerArgumentClass(object):
    """
    A class which takes only integer arguments during init.

    """
    def __init__(self, *args):
        for arg in args:
            if not (isinstance(arg, int) and arg >= 0):
                raise ValueError(arg)
