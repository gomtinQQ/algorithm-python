'''
1544 : [기초-함수작성] 함수로 * n개 출력하기
int 형 자연수(n)가 입력된다.
(1 <= n <= 100)
n개의 *을 한 줄로 출력한다.
'''
def f(n):
    for i in range(n):
        print("*", end="")

n = int(input())
f(n)