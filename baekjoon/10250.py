# 10250. ACM 호텔
cnt = int(input())

for _ in range(cnt):
    h, w, cust = map(int, input().split())
    room = cust//h   # 몫을 정수로 반환
    floor = cust%h
    if h > 1 and floor > 0: room+=1
    if floor == 0: floor = h
    
    print(floor*100 + room)
