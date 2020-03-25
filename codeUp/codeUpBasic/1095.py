'''
1095 : [기초-1차원배열] 이상한 출석 번호 부르기3(설명)
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
'''
n = int(input())
list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])

print(min(list))