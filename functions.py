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

#2nd function here: taking any number of arguments -> number of args with len(args). 
#This works bc *args stores all arguments in a tuple (ordered and immutable collection)
def func2(*args):
    match args:
        case args if len(args) < 2:
            return str(args)
        case args if len(args) == 2:
            func1(*args)
        case args if len(args) > 2:
            return list(map(int, args)) #apparently you do not use *args here
            
            
#def func3(*args):    
func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)
