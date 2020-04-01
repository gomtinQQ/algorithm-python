'''
1540 : [기초-함수작성] 함수로 zero 또는 non zero 출력하기
0 이 입력되면 zero, 그 외에는 non zero를 출력한다.
'''
def f(n):
    if(n==0):
        print("zero")
    else:
        print("non zero")

n = int(input())
f(n)