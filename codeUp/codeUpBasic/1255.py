'''
1255 : 두 실수 사이 출력하기
소수 둘째 자리의 두 실수 a와 b가 입력으로 주어진다.
a와 b사이의 수를 0.01간격으로 오름차순으로 출력하시오.
예) 5.67 5.73  ==> 5.67 5.68 5.69 5.70 5.71 5.72 5.73
'''
a, b = input().split()
a = float(a)
b = float(b)

result = a
while(1):
    if(result>b):
        break
    else:
        print('%.2f' % result)
        result+=0.01

