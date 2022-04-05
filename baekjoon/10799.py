# 10799. 쇠막대기
# 프로그래머스 스터디에서 풀었더 문제. replace가 key 아이디어임.
arrangement = input()
answer = 0 
stack = 0
for paren in arrangement.replace('()', '|'): 
    if paren == '(': # 쇠막대기의 시작 
        stack += 1 
    elif paren == '|': # 레이저 발사 
        answer += stack 
    else: # 쇠막대기 끝 
        stack -= 1 
        answer += 1 # 닫히면 쇠막대기가 하나 추가됨 
print(answer)
