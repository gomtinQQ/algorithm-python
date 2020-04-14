'''
문제: 소수 찾기

문제 설명:
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건:
1) n은 2이상 1000000이하의 자연수입니다.
'''

def solution(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정 후 시작
    lst = [False if i<2 else True for i in range(n+1) ]

    x = int((n ** 0.5))
    for i in range(2, x+1):
        for j in range(2*i, n+1, i):
            lst[j] = False
    return lst.count(True)

n = int(input())
print(solution(n))
