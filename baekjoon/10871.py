# 10871.  X보다 작은 수
# queue 사용함
num, tgt = map(int, input().split())
cmp_num = list(map(int, input().split()))
answer = []
for c in cmp_num:
    if c < tgt:
        answer.append(str(c))

print(' '.join(answer))
