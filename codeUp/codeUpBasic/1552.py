'''
1552 : [기초-함수작성] 함수로 소수 부분만 리턴하기
실수(real number)를 입력 받아 소수 부분만 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성해 제출하시오.

def f(n):
    myNum = n.split('.')
    result = '0.'+myNum[1]
    return float(result)

n = input()
print('{0:0<16}'.format(f(n)))
'''
def f(n):
    result = float(n)
    int_n =  int(float(n))
    return result-int_n

n = input()
print('%0.14f'%f(n))
