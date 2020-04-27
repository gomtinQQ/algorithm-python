'''
문제: 실패율

문제 설명:
실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한 사항:
1) 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
2) stages의 길이는 1 이상 200,000 이하이다.
3) stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
4) 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
5) 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
6) 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
7) 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

'''
def solution(N, stages):
    failureRatio = {} # 실패율
    stayUser = [] # stage에 도달했지만 clear하지 못한 사람 수
    passUser = [] # stage별 clear한 사람 + stage에 도달한 사람
    dictNum = 1

    for i in range(1, N+1):
        cnt = 0
        s = stages.count(i)
        stayUser.append(s)
        for j in stages:
            if j > i:
                cnt += 1
        passUser.append(cnt + s)

    for s, p in zip(stayUser, passUser):
        if s!=0 and p == 0:
            failureRatio[dictNum] = 0
        elif s==0 and p==0:
            failureRatio[dictNum] = 0
        else:
            failureRatio[dictNum] = s/p
        dictNum += 1

    def f(x):
        return x[1]

    answer = [x[0] for x in sorted(failureRatio.items(), key=f, reverse=True)]
    return answer

N = int(input())
stages = list(map(int, input().split()))
print(solution(N, stages))