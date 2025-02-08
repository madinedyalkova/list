list = ["blue","green","red"]
list[0] = "blueberry"
print(list)

#to change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.

list[1:3] = "banana", "tomato"
print(list)

#insert()
list = ["blue","green","red"]
list.insert(2, "kiwi")
print(list)
