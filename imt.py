# (1) Lambda 
# lambda exprestion

a = lambda b: b * 10
print (a(5))

a = lambda a,b: a+b  # a and b are parameters and a+b is the expression
print(a(5,5))

# (2) Map
# map
# purpose apply to function to all items in an iterable e.g( List, tuple, set,etc) and return a new iterable
# syntax: map(function, iterable)

a = [1,2,3,4,5]
l = []
for i in a:
    l.append(i*1)
print(l)

#Use of map function 1st method
a = [1,2,3,4,5]
l = map(lambda b: b+1, a)
print(list(l))

# Method 2nd
def f_name(value):
    return value * 10
a = [1,2,3,4,5]
l = map(f_name, a)
print(list(l))
   

# (3) Filter
# purpose: filter function is used to filter the items in an iterable based on a condition 
# syntax: filter(function, iterable)

def is_even(n):
    return n % 2 == 0
a = [1,2,3,4,5]
l = filter(is_even, a)
print(tuple(l))

# 2nd
a = [10,20,3,0,5]
l = filter(lambda b : b+4 ,a)
print(list(l))

# (3) Zip
# purpose : combin multiple iterable into pairs of elements
# syanx : zip(iterable1, iterable2,......)

name = "Rahul","Ayush","Adarsh","karan","Anjali"
age = [25,45,20,48,55]
l = zip(name,age)
print(list(l))

a = [1,2,3,4,5,6,7,8,9]
l = []
for i in a:
    if i%2==0:
        l.append(i)
print(l)

# write the shorted code even number
# List
a = [1,2,3,4,5,6,7,8,9]
l = [i for i in a if i%2 == 0 ] # 1st append, than loop ,than candition, than logic
print(l)

#(2) tuple
a = [1,2,3,4,5,6,7,8,9]
l = (i for i in a if i%2==0)
print(tuple(l))

# (3) dict
a = [1,2,3,4,5,6,7,8,9]
l = {i:i**2 for i in a if i%2== 0} #dict to add the key value and appened than loop, candition, logic
print(l)