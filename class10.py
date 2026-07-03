# Sets---
s = {10,20,30,40,50}
# print(type(s))
#  you can only store hashable values inside set-

# No duplicate values in setts and unordered nature---

s = {10,20,30,40,50,80,60}
print(s)# unorderd nature--

# no duplicate values--

s = {10,10,10,20,20,30,30,40,30}

print(s)

#  set costructor--
a = [12,12,12,34,35,37,67,67,4,4,4,4,4]

s = set(a)
print(s)

# set traversing---
s = {12,24,78,78,12,23}

for i in s:
    print(i)

#  methods in set--

s = {10,20,30}

s.add(70)
print(s)

# 2 . clear---
s = {10,20,30}
s.clear()
print(s)

# difference---
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s2-s1)

# discard---
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1.discard(10)
print(s1)

# Union--

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1 | s2)