''''
1276 : 팩토리얼 계산
팩토리얼(!)은 다음과 같이 정의된다.
n! = n * (n-1) * (n-2) * ... * 2 * 1
즉, 5! = 5 * 4 * 3 * 2 * 1 = 120 이다.
n이 입력되면 n!의 값을 출력하시오.
'''
n = int(input())
result = 1
for i in range(n, 1, -1):
    result *= i
print(result)