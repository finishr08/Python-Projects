"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

7. How can you use deque to efficiently implement a queuewith a maximum size,
where adding a new element to a full queue removes the oldest element?
"""
from collections import deque

# Define the maximum size of the queue
max_size = 3

# Create a deque object with the maximum size
queue = deque(maxlen=max_size)

# Add some elements to the queue
queue.append(1)
queue.append(2)
queue.append(3)
# Add a new element to the full queue
queue.append(4)

# The oldest element 1 has been removed and the new queue is [2, 3, 4]
print(queue)
