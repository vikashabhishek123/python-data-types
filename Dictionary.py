today we will cover dictionary in python

chai_types={"Black": "Strong", "Green": "Mild", "Oolong": "Rich"}
print(chai_types)

chai_types["Green"]="Delicate"

for chai in chai_types:
    print(chai, chai_types[chai])


if "Black" in chai_types:
    print("Black tea is available")

    else:
    print("Black tea is not available")

#  chai_types["White"]="Smooth"       ("this will add a new key-value pair to the dictionary")

chai_types.pop("Oolong")  # this will remove the key-value pair with key "Oolong"

chai_types.clear()  # this will remove all key-value pairs from the dictionary
chai_types.update({"Herbal": "Soothing", "Chai Latte": "Creamy"})  # this will add new key-value pairs to the dictionary
del chai_types["Green"]  # this will remove the key-value pair with key "Green"

tea_shop={
    "chai":{"Masala":"Spicy", "Ginger":"Zesty"},
    "coffee":{"Espresso":"Strong", "Latte":"Creamy"},
    "pastries":{"Croissant":"Flaky", "Muffin":"Soft"}
    }

    squared_numbers={x:x**2 for x in range(6)}  # this will create a dictionary with numbers from 1 to 5 as keys and their squares as values
print(squared_numbers)
