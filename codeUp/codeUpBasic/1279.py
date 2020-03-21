'''
1279 : 홀수는 더하고 짝수는 빼고 1
두 자연수 a, b 사이의 구간에 대해서
홀수는 더하고 짝수는 뺀다음의 합을 출력하시오.
예)
a = 5, b=10 일 경우, 5 - 6 + 7 - 8 + 9 - 10 = -3
'''
a, b = input().split()
a = int(a)
b = int(b)
sum = 0

for i in range(a, b+1):
    if(i%2==0):
        sum-=i
    else:
        sum+=i
print(sum)
