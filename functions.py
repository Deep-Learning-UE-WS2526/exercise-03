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


def func2 (*a):
  if len(a) < 2:
    return "Das sind " + str(len(a)) + " Elemente."
  if len(a) == 2:
    return func1(a[0], a[1])
  if len(a) > 2:
    return len(a)
    
print(func2(1))
print(func2(1, 2))
print(func2(1, 2, 3))
 


def func3 (**b):

  for key in b:
    if key == "a" or key == "b":
      return func1(b["a"], b["b"])

print(func3(a = "eins", b = "zwei", c = "drei" ))
    
      

# Next, write a function `func3` that takes an arbitrary number of named arguments. 
# Check that two of these arguments have the names `a` and `b`. 
# If so, pass them into `func1`. If not, pass all names of the arguments into `func2`.







  
  


#Write a function func2 that takes an arbitrary number of arguments. 
#In the function, check the number of arguments. 
# If there are less than two arguments, return a string with the number of arguments. 
# If there are two arguments, pass them to func1. 
# If there are more than two arguments, return the number of arguments as an int value.
