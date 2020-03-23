'''
1286 : 최댓값, 최솟값
5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.
'''
list = []
for i in range(5):
    list.append(int(input()))

list.sort()

print(list[4]) # 최댓값
print(list[0]) # 최솟값

