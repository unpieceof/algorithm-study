# 11866. 요세푸스 문제 0
k, n = map(int, input().split())
org_list = [str(num + 1) for num in range(k)]
ans_list = []
rm_idx = 0

for i in range(k):
    rm_idx+=n-1
    if rm_idx >= len(org_list):
        rm_idx = rm_idx%len(org_list) # idx가 배열의 길이보다 커지면 처리
    ans_list.append(org_list.pop(rm_idx))

print("<" + ', '.join(ans_list) + ">")
