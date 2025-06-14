cars = ["toyota", "honda", "ford"]
cars.append("bmw")
print(cars)

languages = ["c++", "swift", "ruby", "javascript"]
languages.insert(2, "python")
print(languages)

fast_food = ["burger", "fries", "pizza"]
desserts = ["cake", "ice cream"]
fast_food.append(desserts.pop(1))
print(fast_food)
print(desserts)

scores = ["90", "85", "70", "100"]
scores.pop(1)
print(scores)

scores_copy = scores.copy()
scores_copy.append("95")
print(scores)
print(scores_copy)

planets = ["mercury", "venus", "earth", "mars"] 
planets.remove("venus")
planets.append("jupiter")
print(planets)


items = ["pen", "pencil", "eraser", "sharpener"]
stationery = []
stationery.append(items.pop(2))
print(stationery)
print(items)

tasks = ["wake up", "brush teeth", "eat breakfast"]
done = []
done.append(tasks.pop(0))
print(done)
print(tasks)
