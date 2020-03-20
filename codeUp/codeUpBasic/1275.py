'''
1275 : k 제곱 구하기
어떤 수 n과 k가 있다.
n과 k의 관계는 다음과 같다.
nk
nk는 n을 k번 곱한 것을 말한다.
입력으로 n과 k가 주어지면 결과를 출력한다.
예)
5^2 = 25
2^4 = 16
'''
n, k = input().split()
n = int(n)
k = int(k)
print(n**k)