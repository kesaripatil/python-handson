import json

person = '{"name":"Kesari", "age":25, "City":"Pune"}'

decodedPerson = json.loads(person)
print(decodedPerson)

fruits = ['apple', 'banana', 'mango']
encodeFruits = json.dumps(fruits)
print(encodeFruits)
print(encodeFruits[2])