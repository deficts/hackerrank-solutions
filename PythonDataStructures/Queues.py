from collections import deque
queue = deque(['Diego','Ilse','Blanca'])

#First In First Out
queue.append('Mario')
print(queue.popleft())
print(queue)
