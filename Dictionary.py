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

