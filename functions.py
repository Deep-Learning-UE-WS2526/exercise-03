def func1(a, b):
  if type(a) == int and type(b) == int:
    print(a+b)
    return a+b
  if type(a) == str and type(b) == str:
    print(b+" "+a)
    return b+" "+a
  if a is None and b is None:
    print("Does not exist.")
    return "Does not exist."
  if type(a) != type(b):
    print(None)
    return None
  print(type(a))
  return type(a)

func1(1,2)
func1("Welt", "Hallo")
func1(None, None)
func1(11, "Freunde")
func1(5.4, 3.6)

def func2(*args):
  if len(args) <2:  
    print(str(len(args)) + " argument(s) provided.")
    return str(len(args))
  if len(args) == 2:
    return func1(args[0], args[1])
  if len(args) > 2:
    print(len(args))
    return len(args)
  
def func3(**kwargs):
  if "a" in kwargs.keys() and "b" in kwargs.keys():
    return func1(kwargs.get("a"), kwargs.get("b"))
  return func2(*kwargs.keys())
  

func2(1)
func2(1,2)
func2(1,2,3,4)
func3(a=5, b=10)
func3(x=1, y=2, z=3)
func3(name="Alice", age=30)
