# 10816. 숫자 카드
s_num = int(input())
s_card = list(map(int, input().split()))
a_num = int(input())
a_card = list(map(int, input().split()))
d = {}

# dictionary.get
for card in s_card:
    d[card] = d.get(card, 0) + 1
    
print(' '.join(str(d[m]) if m in d else '0' for m in a_card))
