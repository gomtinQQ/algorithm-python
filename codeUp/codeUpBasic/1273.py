'''
1273 : 약수 구하기
자연수 N이 주어지면 N의 약수를 오름차순으로 모두 출력하시오.
'''
n = int(input())
N = int(n)

def factor(N):
    result = []
    for i in range(1, N+1):
        if(N%i==0):
            result.append(i)
    return result

num_list = factor(N)
for i in range(len(num_list)):
    print(num_list[i], end=" ")