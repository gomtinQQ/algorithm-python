'''
1548 : [기초-함수작성] 함수로 학점 리턴하기
다음과 같이, 점수를 입력 받아 학점을 출력하시오.

90 점 이상 ~ 100점 이하 : A
80 점 이상 ~ 90점 미만 : B
70 점 이상 ~ 80점 미만 : C
60 점 이상 ~ 70점 미만 : D
60 점 미만 : F
'''
def grade(score):
    if(100 >= score >= 90):
        return 'A'
    elif(90 > score >= 80):
        return 'B'
    elif(80 > score >= 70):
        return 'C'
    elif(70 > score >= 60):
        return 'D'
    else:
        return 'F'

score = int(input())
print(grade(score))