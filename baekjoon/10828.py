# 10828. 스택
import sys

num = int(input())
stack = []

def push(stack, val):
    stack.append(val)

def empty(stack):
    if len(stack) == 0:
        return 1
    else: return 0
    
def top(stack):
    if empty(stack):
        print(-1)
    else:
        print(stack[-1])

def size(stack):
    print(len(stack))

def pop(stack):
    if empty(stack):
        print(-1)
    else:
        top(stack)
        stack.pop()

for _ in range(num):
    fnc = sys.stdin.readline().strip().split()
    
    if fnc[0] == 'push':
        push(stack, fnc[1])
    elif fnc[0] == 'empty':
        print(empty(stack))
    elif fnc[0] == 'top':
        top(stack)
    elif fnc[0] == 'size':
        size(stack)
    elif fnc[0] == 'pop':
        pop(stack)
    else:
        print('Error')
