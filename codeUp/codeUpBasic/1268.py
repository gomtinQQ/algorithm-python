'''
1268 : n개의 수 중 짝수의 개수
수의 개수 n이 주어지고, 그 다음 줄에 무작위로 n개의 자연수가 입력된다.
그 n개의 수 중에서 짝수의 개수를 출력하시오.
'''
n = int(input())
num_list = input().split()
cnt = 0

for i in range(len(num_list)):
    if(int(num_list[i])%2==0):
        cnt+=1

print(cnt)