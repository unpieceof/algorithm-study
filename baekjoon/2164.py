# 2164. 카드2
from collections import deque
cards = deque()

def pop_card(cards):
	cards.popleft()
	card = cards[0]
	cards.popleft()
	cards.append(card)

num = int(input())
for i in range(num):
	cards.append(i+1)

while(len(cards) > 1):
	pop_card(cards)

print(cards[0])
