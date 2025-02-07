#items are indexed and we can access them by referring to the index number.

color = ["blue","red","orange"]
print(color[1])

#we can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new list with the specified items.
color = ["blue","red","orange","green"]
print(color[1:3])

#by leaving out the start value, the range will start at the first item.
print(color[:3])
