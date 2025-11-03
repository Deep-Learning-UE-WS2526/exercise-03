x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [i*2 for i in x] # all elements of `x`, multiplied by 2
print(a)
b = [i for i in x if i%2==0] # all even elements of `x`
print(b)
c = [x for x in y if x==True] # all truish elements of `y` (i.e., all elements that evaluate to `True` in a boolean context)
print(c)
d = [x for x in y if isinstance(x, str)] # all string elements of `y`
print(d)
e = [[True for i in range(ee)] for ee in x if ee%2!=0] # contains a list for each odd element of `x`
print(e)

