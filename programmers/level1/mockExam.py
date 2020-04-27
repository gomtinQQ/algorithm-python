'''
문제: 모의고사
문제 설명:
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건:
1) 시험은 최대 10,000 문제로 구성되어있습니다.
2) 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
3) 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
    # 0 0 0 0 2 0 0 0 0 0 3
'''

def solution(answers):
    p = len(answers)

    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000

    s1 = s1[:p]
    s2 = s2[:p]
    s3 = s3[:p]

    a_list = [0, 0, 0]
    result = []

    for i in range(p):
        if s1[i] == answers[i]:
            a_list[0] +=1
        if s2[i] == answers[i]:
            a_list[1] += 1
        if s3[i] == answers[i]:
            a_list[2] += 1


    maxScore = max(a_list)

    if maxScore == 0:
        reslut = [1,2,3]

    for i in range(len(a_list)):
        if a_list[i] == maxScore:
            result.append(i+1)

    return result

answers = list(map(int, input().split()))
print(solution(answers))