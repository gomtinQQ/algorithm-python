'''
1537 : [기초-함수작성] 함수로 hello 또는 world 출력하기
hello 또는 world 를 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성하시오.
1 이 입력되면 hello, 2 가 입력되면 world 를 출력한다.
'''
def f(n):
    if(n==1):
        print("hello")
    else:
        print("world")

n = int(input())

f(n)