def func1(a, b):
  if type(a) == int and type(b) == int:
    return a+b
  if type(a) == str and type(b) == str:
    return b+" "+a
  if a is None and b is None:
    return "Does not exist."
  if type(a) != type(b):
    return None
  return type(a)

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

def func2(*args):
    numArgs = len(args)
    if numArgs < 2:
        return str(numArgs)
    if numArgs == 2:
        return func1(args[0], args[1])
    if numArgs > 2:
        return numArgs
    
def func3(**kwargs):
    a = b = False
    for key in kwargs:
        if key == "a":
            a = True
        elif key == "b":
            b = True
    if a and b:
        return func1(kwargs["a"], kwargs["b"])
    else:
        return func2(kwargs)
