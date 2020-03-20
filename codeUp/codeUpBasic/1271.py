''''
1271 : 최대값 구하기
입력의 개수 n이 입력되고 n개의  데이터가 입력된다.
이 n개의 데이터 중 최대값을 출력한다.
'''
n = int(input())
num_list = input().split()
result = 0

for i in range(n):
    result = max(result, int(num_list[i]))

print(result)