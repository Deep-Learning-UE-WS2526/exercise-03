x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

# A list called `a` that contains all elements of `x`, multiplied by 2.
a = [item * 2 for item in x]

# A list called `b` that contains all even elements of `x`.
b = [item for item in x if item % 2 == 0]

# A list called `c` that contains all truish elements of `y`.
c = [item for item in y if bool(item)]

# A list called `d` that contains all string elements of `y`.
d = [item for item in y if isinstance(item, str)]

# A list called `e` that contains a list for each odd element of `x`.
# Each inner list contains `True` repeated `n` times where `n` is the odd value.
e = [[True] * item for item in x if item % 2 == 1]

if __name__ == '__main__':
	print("a:", a)
	print("b:", b)
	print("c:", c)
	print("d:", d)
	print("e:", e)

