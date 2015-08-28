__author__ = 'brapastor'

from collections import deque

queue = deque(['eric','jhon','brayan'])
queue.append("Terry")
queue.append("joao")
queue.popleft() # el primero el llegar ahora se va
queue.popleft() # el primero el llegar ahora se va
print(queue)

