#friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
#print(friends)

numbers = [18, 25, 1, -15, 69, 78, 45, 32]
print(numbers)

#Checking if an element is in the list
#if "Ahmed" in friends:
    #print("Friend is in list")
#else:
    #print("Friend not in list")
    
#Checking how many items in list
#print(len(friends))

#Adding an item to your list
#friends.append("Ahmed")
#print(friends)

#Adding an item to list at a certain index
#friends.insert(0, "Paul")
#print(friends)

#Removing an item from list
#item = friends.pop()
#print(item)
#print(friends)

#Removing an item from list
#item = friends.remove("Karen")
#print(friends)

#Clearing a list
#friends.clear()
#print(friends)

#Arranges list in reverse order
#friends.reverse()
#print(friends)

#Arranges a list in asencding order
#numbers.sort()
#print(numbers)

#Combining two lists
#new_list = friends + numbers
#print(new_list)

#Prints items from list in range
#a = numbers[1:6]
#print(a)

#Prints every second value in a list
#a = numbers[::2]
#print(a)

#A way of creating a new list from an existing one
#Prints the cube values of a list
cubes = [i*i*i for i in numbers]

print(cubes)