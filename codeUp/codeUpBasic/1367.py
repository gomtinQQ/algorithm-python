'''
1367 : 평행사변형 출력하기 1
평행사변형의 높이 n이 주어진다.
옆 면이 대각선으로 이루어지는 평행사변형을 출력한다.
단,공백은 왼쪽 위에 있다.
'''
n = int(input())
for i in range(1, n+1):
    for k in range(n-i, 0, -1):
        print(" ", end="")
    for k in range(n):
        print("*", end="")
    print()