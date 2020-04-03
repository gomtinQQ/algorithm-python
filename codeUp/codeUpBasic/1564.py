'''
1564 : [기초-함수작성] 함수로 최대공약수 리턴하기
int 형 자연수 두 개를 입력받아
최대공약수(GCD, Greatest Common Divisor)를 출력하시오.
단, 함수형 문제이므로 함수gcd()만 작성하여 제출하시오.
'''
def gcd(x, y):
    num = 0
    if(x > y):
        max = x
        min = y
    else:
        max = y
        min = x

    for i in range(1, min+1):
        if(x%i==0 and y%i==0):
            num = i
    return num

x, y = input().split()
x = int(x)
y = int(y)
print(gcd(x, y))

