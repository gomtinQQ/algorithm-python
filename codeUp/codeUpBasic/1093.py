'''
1093 : [기초-1차원배열] 이상한 출석 번호 부르기1(설명)
출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

'''
n = int(input())
name_call = input().split()
call_count = []

# 빈 배열 만들기
for i in range(23):
    call_count.append(0)

# 출석 번호 count
for i in range(n):
    number = int(name_call[i])-1
    call_count[number] = call_count[number] + 1

for i in range(len(call_count)):
    print(call_count[i], end=" ")