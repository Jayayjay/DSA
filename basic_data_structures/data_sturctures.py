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

# List comprehensions

squares = []
for i in range(11):
    squares.append(i**2)
    
squares

squares = list(map(lambda x:x**2, range(10)))
# same as 
squares = [x**2 for x in range(10)]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

combs