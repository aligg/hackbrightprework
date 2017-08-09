animals = ["cat", "dog,", "unicorn", "rat", "mouse", "deer", "grouse", "fish", "whale", "kangaroo"]
k_list = []

for animal in animals:
    if animal.startswith("k"):
        k_list.append(animal)
print k_list 