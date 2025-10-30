x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [x*2 for x in x ]
b = [x for x in x if x%2 == 0]
c = [x for x in y if x == True]
d = [x for x in y if x == str]
e = [[True]*x for x in x if x%2 == 1]

print(e)




