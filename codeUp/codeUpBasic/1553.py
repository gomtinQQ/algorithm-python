'''
1553 : [기초-함수작성] 함수로 정수 올림 한 값 리턴하기
실수(real number)를 입력 받아 정수로 올림해 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성해 제출하시오.
'''
import math
def f(n):
    return '%d' %math.ceil(float(n))

n = input()
print(f(n))