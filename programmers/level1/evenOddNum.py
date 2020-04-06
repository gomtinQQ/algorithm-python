'''
문제: 짝수와 홀수
문제 설명: 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, solution을 완성해주세요.
제한 조건 :
1) num은 int 범위의 정수입니다.
2) 0은 짝수입니다.
시간 : 1m 58s
'''
def solution(num):
    answer = ''
    if(num%2==0):
        answer = "Even"
    else:
        answer = "Odd"
    return answer

number = int(input())
print(solution(number))