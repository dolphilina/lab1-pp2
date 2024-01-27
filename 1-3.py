car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
print(car.get("year"))
car["year"] = 2020
print(car.get("year"))
car["color"] = "red"
car.pop("model")
car.clear()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
for x in fruits:
    if x == "banana":
        continue
    print(x)
for x in range(6):
    print(x)
for x in fruits:
  if x == "banana":
    break
  print(x)