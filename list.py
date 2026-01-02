squares1to5 = [1, 4, 9, 16, 25]
squares6to10 = [36, 49, 64, 81, 100]

squares1to10 = squares1to5 + squares6to10
squares2to6 = squares1to10[1:6]

print(f"{squares1to5} + {squares6to10} = {squares1to10}")
print(f"squares2to6 is: {squares2to6}")

print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
fruits = ["apple", "banana", "mango"]
print("Fruits list")
print(fruits)

fruits.pop()
print("Fruits list after pop")
print(fruits)

fruits.clear()
print("Fruits list after clear")
print(fruits)

del fruits
print("Fruits list after delete")
#print(fruits) 
print("No variable is in existance:)")

print("------------------------------------------------------------------")
print("------------------------------------------------------------------")
animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # Create a new list
print(animals)

animals[1:3] = ["cat"]    # Replace 2 items -- "lion" and "tiger" with one item -- "cat"
print(animals)

animals[1:3] = []     # Remove 2 items -- "cat" and "giraffe" from the list
print(animals)

animals[1] = "elephant"
animals[2] = "elephant"
print(animals)

