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

# func1(1,2)
# func1("Welt", "Hallo")
# func1(None, None)
# func1(11, "Freunde")
# func1(5.4, 3.6)

def func2(*args):
   numArgs = len(args)
   if numArgs < 2:
     return str(numArgs)
   if numArgs == 2:
     return func1(args[0], args[1])
   if numArgs > 2:
     return numArgs

print("func2:")
print(func2(8))
print(func2(5,5))
print(func2(2,5,3))

def func3(**kwargs):
  if all(key in kwargs for key in("a", "b")):
    return func1(kwargs.get("a"), kwargs.get("b"))
  else: 
    args = []
    for value in kwargs.values():
      args.append(value)
    return func2(*args)

print("func3")
print(func3(a= 2, b=5))
print(func3(a = "world", b = "hello"))
print(func3(a = 5, b = 10, c = 15))
print(func3(d = 2, x = 10))