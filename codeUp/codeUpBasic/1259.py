'''
1259 : 1부터 n까지 중 짝수의 합 구하기
1부터 n까지의 수 중 짝수의 합을 구하시오.
'''
n = int(input())
n = int(n)
sum = 0

for i in range(1, n+1):
    if(i%2==0):
        sum += i
print(sum)
