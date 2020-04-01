'''
1539 : [기초-함수작성] 함수로 false 또는 true 출력하기
0 이 입력되면 false, 그 외에는 true를 출력한다.
단, 함수형 문제이므로 함수 f()만 작성하시오.
'''
def f(n):
    if(n==0):
        print("false")
    else:
        print("true")

n = int(input())
f(n)