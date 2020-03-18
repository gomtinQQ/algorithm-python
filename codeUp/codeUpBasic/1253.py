'''
1253 : a 부터 b까지 출력하기
어떤 두 수 a, b가 있을 때 두 수 사이의 모든 정수를 오름차순으로 출력하시오.
예를 들어, a=5 , b=10일 경우 5 6 7 8 9 10입니다.
'''
a, b = input().split()
a = int(a)
b = int(b)
if(a<b):
    min = a
    max = b
else:
    min = b
    max = a
for i in range(min, max+1):
    print(i, end = " ")