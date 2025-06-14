# fruits = ["apple", "pineapple", "blueberries", "grapes"]

# fruits.append("orange")
# print(fruits)
# fruits.insert(1, "pear")
# print(fruits)
# fruits.extend(["cranberry", "mangoe", "kiwi"])
# print(fruits)
# fruits += ["guava", "watermellon"]
# print(fruits)


# fruits.remove("blueberries")
# print(fruits)
# print(fruits.pop(2))
# print(fruits)

# books2_read = ["harry potter", "bible", "children books" ]
# books_read = ["to kill a mockingbird", "1984", "the alchemist"]
# books_read.append(books2_read.pop())
# print(books_read)
# print(books2_read)


# fruits2 = fruits.copy()
# fruits2.append("fig")
# print(fruits2)
# print(fruits)

import copy
cars = [["corolla", "camry"], ["accord", "civic"], ["mustang", "F150"]]
cars_2 = copy.deepcopy(cars)
cars_2[1].append("pilot")
print(cars)
print(cars_2)
