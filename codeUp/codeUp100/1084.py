'''
1084 : [기초-종합] 빛 섞어 색 만들기(설명)
빨강(red), 초록(green), 파랑(blue) 빛을 섞어
여러 가지 빛의 색을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
(빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)

주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과
총 가짓 수를 계산해보자.
'''
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            count +=1
            print(i, j, k)

print(count)