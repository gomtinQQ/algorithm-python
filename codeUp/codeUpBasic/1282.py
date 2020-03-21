'''
1282 : 제곱수 만들기
n이 입력되면 k를 빼서 제곱수를 만들 수 있는 k를 구하고,
그 제곱수에 루트를 씌운 수(제곱근) t를 구하여라.
이 때 k는 여러가지가 될 수 있는데 가장 작은 k를 출력한다.
'''
import math
n = int(input())
num = 0


for i in range(1, n+1):
    if(i**2==n):
        num = i
        break
    elif(i**2>n):
        num = i-1
        break
    else:
        continue

k = n - num**2
t = num
print(k, int(t))

