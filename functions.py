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
 

def func2(*args):
  """Handle a variable number of positional arguments.

  - If less than two arguments: return a string with the number of arguments.
  - If exactly two arguments: pass them to func1 and return the result.
  - If more than two arguments: return the number of arguments as an int.
  """
  n = len(args)
  if n < 2:
    return str(n)
  if n == 2:
    return func1(args[0], args[1])
  return n


def func3(**kwargs):
  """Handle a variable number of named arguments.

  - If kwargs contains both 'a' and 'b', pass them to func1.
  - Otherwise, pass all argument names (strings) to func2.
  """
  if 'a' in kwargs and 'b' in kwargs:
    return func1(kwargs['a'], kwargs['b'])
  # pass all names of the arguments into func2
  names = list(kwargs.keys())
  return func2(*names)


if __name__ == '__main__':
  # demonstrations (showing the different return modes)
  print(func1(1,2))                # ints -> sum
  print(func1("Welt", "Hallo")) # strings -> concat (b + ' ' + a)
  print(func1(None, None))         # both None -> message
  print(func1(11, "Freunde"))    # different types -> None
  print(func1(5.4, 3.6))           # unmatched same type -> return type

  # func2
  print(func2())                   # less than two -> string '0'
  print(func2(10))                 # less than two -> string '1'
  print(func2(2,3))                # two args -> passed to func1 -> 5
  print(func2(1,2,3))              # more than two -> int 3

  # func3
  print(func3(a=5, b=7))           # has a and b -> func1(5,7) -> 12
  print(func3(x=1, y=2))           # no a/b -> pass names to func2 -> func2('x','y') -> func1('x','y') -> 'y x'