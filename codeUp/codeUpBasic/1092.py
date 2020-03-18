'''
1092 : [기초-종합] 함께 문제 푸는 날(설명)

같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다.
(단, 입력값은 100이하의 자연수이다.)
3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

최대공약수 (GCD : Greatest Common Divisor)
최소공배수 (LCM : Least Common Multiple)
'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

#최대공약수(GCD)를 구하는 함수
def gcd(x,y):
    if(x>y):
        min = y
    else:
        min = x
    for i in range(1, min+1):
        if(x%i==0 and y%i==0):
            result = i
    return result

#최소공배수(LCM)을 구하는 함수
def lcm (x,y, gcdNum):
    result = int((x*y)/gcdNum)
    return result

#a, b의 최소공배수를 구한다.
gcdNum = gcd(a,b)
lcmNum = lcm(a,b, gcdNum)

#(a,b), c의 최소공배수를 구한다.
gcdResult = gcd(lcmNum, c)
result = lcm(lcmNum, c, gcdResult)
print(result)
