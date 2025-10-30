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
    return
    
def func3(**kwargs):
    a = b = False
    key1 = key2 = ""
    for key in kwargs:
        if key == "a":
            a = True
            key1 = key
        elif key == "b":
            b = True
            key2 = key
    if a == True and b == True:
        return func1(key1, key2)
    else:
        return func2(kwargs)
    return
