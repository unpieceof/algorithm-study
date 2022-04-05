# 9012. 괄호
# 프로그래머스 올바른 괄호와 유사한 문제
def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return count == 0

n = input()
answer = [0]*int(n)
for i in range(int(n)):
    vps = input()
    if solution(vps) == True:
        answer[i] = "YES"
    else:
        answer[i] = "NO"

for ans in answer:
    print(ans)
