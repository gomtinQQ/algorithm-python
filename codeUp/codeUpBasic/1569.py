'''
1569 : [기초-함수작성] 함수로 배열의 최대값 위치 리턴하기 2
데이터가 오름차순으로 저장되어있는 배열에서
원하는 데이터가 저장되어있는 가장 처음 위치를 출력하시오.
(원하는 데이터가 저장되어있지 않은 경우 –1을 출력한다.)

단, 함수형 문제이므로 함수 findi()만 작성하여 제출하시오.

예를 들어 1번 자리부터 10개의 데이터가 오름차순으로 저장되어있는 배열
2 3 5 7 11 13 17 19 23 27 에서
값 11 의 위치는 5 이다.
값 12 는 저장되어있지 않으므로 –1을 출력한다.
'''
def findi(a):
    answer = -1
    a_lst.sort()

    for i in range(len(a_lst)):
        if(a_lst[i] == a):
            return i+1

    return answer

n = int(input())
a_lst = map(int, input().split())
a_lst = list(a_lst)
a = int(input())

print(findi(a))