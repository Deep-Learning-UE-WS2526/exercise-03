def func1(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    if type(a) == str and type(b) == str:
        return b + " " + a
    if a is None and b is None:
        return "Does not exist."
    if type(a) != type(b):
        return None
    return type(a)


def func2(*args):
    n = len(args)
    if n < 2:
        return str(n)           
    if n == 2:
        return func1(args[0], args[1])
    return n                   

def func3(**kwargs):
    if 'a' in kwargs and 'b' in kwargs:
        return func1(kwargs['a'], kwargs['b'])
   
    return func2(*kwargs.keys())

