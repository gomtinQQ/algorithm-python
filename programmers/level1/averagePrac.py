'''
문제: 평균 구하기
문제 설명: 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
제한 사항:
1) arr은 길이 1 이상, 100 이하인 배열입니다.
2) arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
'''
def solution(arr):
    answer = 0
    sumNum = sum(arr)

    if(sumNum==0):
        return 0

    answer = sumNum/len(arr)
    return answer

arr = map(int, input().split())
arr = list(arr)
print(solution(arr))