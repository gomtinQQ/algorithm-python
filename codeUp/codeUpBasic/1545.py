'''
1545 : [기초-함수작성] 함수로 true(1) / false(0) 리턴하기
int 형 정수(n)가 입력된다.
(-2147483648 <= n <= 2147483647)
0 이 입력되면 zero, 그 외에는 non zero 를 출력한다.
'''
def f(n):
    if(n==0):
        return True
    else:
        return False

n = int(input())
if(f(n)):
    print("zero")
else:
    print("non zero")