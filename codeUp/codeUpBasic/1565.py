'''
1565 : [기초-함수작성] 함수로 최소공배수 리턴하기
int 형 자연수 두 개를 입력받아
최소공배수(LCM, Least Common Multiple)를 출력하시오.
단, 함수형 문제이므로 함수 lcm()만 작성하여 제출하시오.
참고
최소공배수는 두 수의 공통 배수들 중에서 가장 작은 공통 배수를 의미한다.
예를 들어 72와 192의 최소 공배수는 576이다.
'''
def lcm(x, y):
    tmp = 1
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x

    while(max%min!=0):
        tmp = max%min
        max = min
        min = tmp

    xt = x/tmp
    yt = y/tmp
    # 최대 공약수
    return int((int(xt)*int(yt))*tmp)

x, y = input().split()
x = int(x)
y = int(y)

print(lcm(x, y))
