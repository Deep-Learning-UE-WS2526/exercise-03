x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

a = [n*2 for n in x]
b = [n for n in x if n % 2 == 0]
c = [n for n in y if n is True or n == "True"]
d = [n for n in y if isinstance(n, str)]
e = [[[True] * n] for n in x if n % 2 != 0]