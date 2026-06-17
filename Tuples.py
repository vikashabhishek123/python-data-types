# in this chapter we will learn about tuples in python

tea_types=("Black", "Green", "Oolong", "White")  # this will create a tuple with the given values
print(tea_types)


tea_types[1]
tea_types[0:2]  # this will return a new tuple with the values from index 0 to 1
len(tea_types)  # this will return the number of elements in the tuple

more_tea =("herbal", "chai latte")  
all_tea=tea_types+more_tea  # this will create a new tuple with the values from both tuples
print(all_tea)

