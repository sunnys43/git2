def deco_fxn(val):
    def outer_fxn(fxn):
        def inner_fxn(*args):
            args = args[0] + val
            return fxn(*args)
        return inner_fxn
    return outer_fxn

        