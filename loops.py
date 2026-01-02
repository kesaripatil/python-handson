number = 1
square = 0
print("Square using for loop")
for number in range(1, 11, 1):
    square = number ** 2
    print(f"{square}")
    number += 1

square = 0
number = 1
print("Square using while loop")
while number <= 10:
    square = number ** 2
    print(f"{square}")
    number += 1


for n in range(2,3):
    print(f"Loop executed for {n}")
    break
else:
    print("Loop didn't execute for given range")

for i in range(2,10):
    for j in range(2,i):
        if i % j == 0:
            print(i, 'equals', j, "*", i//j)
            break
    else:
        print(i, " is prime number")
