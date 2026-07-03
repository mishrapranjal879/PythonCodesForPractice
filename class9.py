# Tuple ----
# tuple has hetrogeneous nature
# tuple has immutable
# tuple can store duplicate values

# Tuple unpacking---

a,b,c = (10,20,30)

print(b)

a = (1)

print(type(a))

# Tuple indexing and slicing--

a = (10,20,30,40,50)

print(a[:3])

#  traversing---
t = (10,20,30,40,50)

for i in t:
    print(i)
for i in range(len(t)):
    print(t[i]) 

# method in tuple    

a = (10,20,30,40,40,40,50,)
print(a.count(40))
print(a.index(30))
