# 10866. 덱
from collections import deque 
import sys

num = int(input())
dq = deque()

def push_front(dq, val):
    dq.appendleft(val)

def push_back(dq, val):
    dq.append(val)

def empty(dq):
    if len(dq) == 0:
        return 1
    else: return 0
    
def back(dq):
    if empty(dq):
        print(-1)
    else:
        print(dq[-1])

def front(dq):
    if empty(dq):
        print(-1)
    else:
        print(dq[0])

def size(dq):
    print(len(dq))

def pop_back(dq):
    if empty(dq):
        print(-1)
    else:
        back(dq)
        dq.pop()

def pop_front(dq):
    if empty(dq):
        print(-1)
    else:
        front(dq)
        dq.popleft()


for _ in range(num):
    fnc = sys.stdin.readline().strip().split()
    
    if fnc[0] == 'push_front':
        push_front(dq, fnc[1])
    elif fnc[0] == 'push_back':
        push_back(dq, fnc[1])
    elif fnc[0] == 'empty':
        print(empty(dq))
    elif fnc[0] == 'front':
        front(dq)
    elif fnc[0] == 'back':
        back(dq)
    elif fnc[0] == 'size':
        size(dq)
    elif fnc[0] == 'pop_front':
        pop_front(dq)
    elif fnc[0] == 'pop_back':
        pop_back(dq)
    else:
        print('Error')