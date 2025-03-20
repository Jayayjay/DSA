# Lists
 # Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['Name']) 

# accessing a element using get() 
# method 
print("Accessing a element using get:") 
print(Dict.get(1)) 

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

# lists as stacks

stack = [1, 3, 4]
stack.append(0)
stack.append(7)
print(stack)
stack.pop(3)
print(stack)

# lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue