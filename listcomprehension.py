x = [0,1,2,3,4,5,6,7,8,9]
y = [True, False, False, True, "False", False, True, True, True, "True"]

#Create 5 EMPTY Lists, but c2 f.ex runs just fine without being created in advance. Printing out d and e  on the other hand without initializing them results in an error  
a,b,c,d,e = ([] for i in range(5)) 

a = [num*2 for num in x]
b = [num for num in x]
#if is needed here
c = [entry for entry in y if entry == True]
#checks for boolean values as well as Strings that spell True
c2 = [entry for entry in y if entry == True or entry == "True"] 
#check if entries in y are of the type String (written as str not String)
d = [entry for entry in y if isinstance (entry, str)]
# list with a list for each odd element in x with the boolean value True. List size equals the current (odd) number of x (1,3,5,7,9) 
#e = [num for num in x if x / 2 != 0]
e = [[True] for x in x if x % 2 !=0] #this does not work I get True whenever the list element is not divisible by 2

#For some reason the output is not displayed on the console, but the online interpreterdisplays it correctly
print(a)
print(b)
print(c)
print(c2)
print(d)
print(e)