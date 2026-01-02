phone_book = {
            "abc" : 123,
            "pqr" : 456,
        }

print(f"Phone Book: {phone_book}")
phone_book["xyz"] = 789
print(f"Add xyz to phone book: {phone_book}")
del phone_book["pqr"]
print(f"Remove pqr from phone book: {phone_book}")

names = ["abc", "pqr", "stu"]
ages  = [10, 11, 12]
students = {}
for x in range(len(names)):
    students[names[x]] = ages[x]
print(f"Student details: {students}")

print(f"Keys of phone book: {phone_book.keys()}")
print(f"Values of phone book: {phone_book.values()}")
print(f"Items of phone book: {phone_book.items()}")
