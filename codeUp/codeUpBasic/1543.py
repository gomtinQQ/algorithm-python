'''
1543 : [기초-함수작성] 함수로 love 출력하기
int 형 자연수(n)가 입력된다.
(1 <= n <= 100)
줄을 바꿔가며 love를 n번 출력한다.
'''
def f(n):
    for i in range(n):
        print("love")

n = int(input())
f(n)