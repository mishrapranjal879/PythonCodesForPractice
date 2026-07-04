# Advance stuff in python ----

# Lambda expression--

# square = Lambda a : print(a**2)

# square(12)

# add = lambda x,y : X+y

# print(add(12,12))

#  mapping--

# purpose apply function to every item of an iterable and return a new item

# syntax = map(function , iterable)

# def square(x):
#     return x**2
# a = [1,2,3,4]

# l = map(lambda x : x **2)

# print(list(l))


# Filter---
# purpose- filter items from an iterable based on a condition

# syntax- filter(function,iterable)

# a = [1,2,3,4,5,6]

# l = filter(lambda x : x%2 == 0,a)

# print(list(l))

# zip--

# purpose - Cobine multiple iterables into pairs of elements

# syntax-- zip(iterable 1, iterable 2,....)

# name = ["Pranjal", "Siddhant", "Shivansh"]
# ages = [24,22,23]

# comb = zip(name,ages)

# print(list(comb))

# generator---
# it save memory for lazy datasets

# Efficient for lazy evaluation (compute values only when  needed)

def my_generator():
    for i in range(5):
        yield(i) 

gen = (my_generator())

print(next(gen))
print(next(gen))