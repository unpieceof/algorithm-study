# 2751. 수 정렬하기 2
# 우선순위 큐 사용하여 해결
import sys
from queue import PriorityQueue
answer = PriorityQueue()

num = int(sys.stdin.readline())
for _ in range(num):
    apple = int(sys.stdin.readline())
    answer.put(apple)

for _ in range(num):
    print(answer.get())
