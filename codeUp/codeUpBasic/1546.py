'''
1546 : [기초-함수작성] 함수로 plus/minus/0 판별하기
정수 1개를 입력 받아
양수인 경우 plus, 음수인 경우 minus, 0 인 경우 0을 판별하여 출력하시오.
단, 함수형 문제이므로 함수 zero()와 plus()만 제출하시오.
int 형 정수(n)가 입력된다.
(-2147483648 <= n <= 2147483647)
양수인 경우 plus, 음수인 경우 minus, 0 인 경우 0을 판별하여 출력하시오.
'''
def zero(n):
    if(n==0):
        return True

def plus(n):
    if(n>0):
        return True
    else:
        return False

n = int(input())
if(zero(n)):
    print("zero")
else:
    if(plus(n)):
        print("plus")
    else:
        print("minus")
