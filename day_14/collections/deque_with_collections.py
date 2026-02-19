from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
print(dq)
