'''
1269 : 수열의 값 구하기
시작값 a, b, c, n이 차례대로 입력된다.
( -9 <= a, b, c < = 9, 1 <= n <= 9)
n번째 수열의 값을 출력한다.
'''
a, b, c, n = input().split()
a = int(a)
b = int(b)
c = int(c)
n = int(n)
result = a

for i in range(n-1):
    result = result * b + c

print(result)