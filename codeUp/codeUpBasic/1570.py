'''
1570 : [기초-함수작성] 함수로 Lower Bound 위치 리턴하기
데이터가 오름차순으로 저장되어있는 배열에서
어떤 값보다 크거나 같은 값이 처음 나타나는 위치를 출력하시오.
(저장되어있는 값들이 입력된 값보다 모두 작다면 저장되어있는 데이터개수+1을 출력한다.)

단, 함수형 문제이므로 함수 lower_bound()만 작성하여 제출하시오.

예를 들어 1번 자리부터 10개의 데이터가 오름차순으로 저장되어있는 배열
2 3 5 7 9 11 13 17 19 23 에서
값 6 보다 크거나 같은 값이 처음 나타나는 위치는 4 이다.
값 24 는 저장되어있는 모든 값들보다 크므로 11 을 출력한다.
'''
def lower_bound(k):
    for i in range(len(n_lst)):
        if(n_lst[i]>=k):
            return i+1
    return n+1

n = int(input())
n_lst = map(int, input().split())
n_lst = list(n_lst)
k = int(input())

print(lower_bound(k))