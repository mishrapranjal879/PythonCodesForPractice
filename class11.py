# Dictionary----

a = {1:10,1:20,2:30}
print(type(a))

# dictionary is mutable and in dictionary only value is changed not key is change

d = {10:100,20:200,30:300}
print(d[10]) # not duplicate keys are allowed

d = dict(name = "pranjal",age = 22,gender = "male")

print(d)

# Traversing in dictionary---

# a = {10:100,20:200,30:300,40:400}

# for i in a:
#     print(a[i])

# Methods in dict.----

# help(dict) 
a = {10:100,20:200,30:300,40:400}

# print(a.get)
print(a.items)
 