# import counter class from collections module
from collections import Counter

#Creating a Counter class object using list as an iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

x = Counter(a)

#directly printing whole x
print(x)

#We can also use .keys() and .values() methods to access Counter class object
for i in x.keys():
      print(i, ":", x[i])
    
#We can also make a list of keys and values of x
x_keys = list(x.keys())
x_values = list(x.values())

print(x_keys)
print(x_values)