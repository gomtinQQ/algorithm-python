'''
1258 : 1부터 n까지 합 구하기
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.
'''
n = int(input())
sum = 0

for i in range(0, n+1):
    sum += i

print(sum)