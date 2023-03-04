stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh")
print("1: ",stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen St")
print("2: ",stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4,"Polmont")
print("3: ",stops)
#4. Print out the index position of "Linlithgow"
# stops.index("Linlithgow") will by default print it to the terminal
print("4: ", stops.index("Linlithgow"))
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print("5: ",stops)
#6. Delete "Cumbernauld" from the list by index
stops.remove(stops[2])
# Solution was to use index to find THE INDEX - 
# stops.pop(stops.index("Cumbernauld"))
print("6: ",stops)
#7. Print the number of stops there are in the list
print("7: ",len(stops))
print("7b: ",stops)
#8. Sort the list alphabetically
stops.sort()
print("8: ",stops)
#9. Reverse the positions of the stops in the list
stops.reverse()
print("9: ",stops)
#10 Print out all the stops using a for loop
for stop in stops:
    print("10: ",stop)

# 