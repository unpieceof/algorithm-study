# 11650. 좌표 정렬하기
# 2차원 배열 정렬
num = int(input())
coords = []

for _ in range(num):
	x, y = map(int, input().split())
	coords.append([x, y])

coords.sort()
for coord in coords:
    print(coord[0], coord[1])
