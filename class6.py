#  While loop-----(basis on the condition)

a = 0

while a<10:
    print(a)

    a = a + 1


    # Conditions in while loop---

    # 1 -- Break
    # 2-- Continue
    # 3-- else

for i in range(1,11):
    print(i)
    if i == 6:
        break


# continue---

for i in range(1,11):
  
    if i == 6:
        continue
    print(i)

# else----

for i in range(1,5):
    if i ==4:
        break
    print(i)

else:
    print("no break execute")
