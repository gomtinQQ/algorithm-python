'''
높이 h와 반복휫수 r이 주어질때, 별을 다음과 같이 지그재그로 출력하자.

예) 3 2

*
 *
  *
 *
*
*
 *
  *
 *
*
'''
h, r = map(int, input().split())

def zigzag(h):
    for i in range(0, h):
        for j in range(0, i):
            print(" ", end="")
        print("*")

    for i in range(h-2, -1, -1):
        for j in range(0, i):
            print(" ", end="")
        print("*")

for i in range(r):
    zigzag(h)
