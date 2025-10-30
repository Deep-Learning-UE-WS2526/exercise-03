x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [ e*2 for e in x]
print(a)

b = [ e for e in x if e%2==0]
print(b)

c = [e for e in y if e == True]
print(c)

d = [ e for e in y if type(e) == str]
print(d)

e = [ [True for i in range(el)] for el in x if el%2!=0]
print(e)