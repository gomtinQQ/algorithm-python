'''
1568 : [기초-함수작성] 함수로 배열의 최대값 위치 리턴하기
배열의 참조 범위([a, b], a번부터 ~ b번까지 범위, 폐구간 [a, b])를 입력 받아
그 범위에서 가장 큰 값이 가장 처음 나타난 위치를 출력하시오.
단, 함수형 문제이므로 함수 maxi()만 작성하여 제출하시오.
예를 들어 1 ~ n번으로 구성된 배열
5 1 4 3 2 에서
폐구간 [2, 4]에서 가장 큰 값이 가장 처음 나타난 위치를 계산하면 3(값 4)가 된다.
'''
def maxi(a, b):
    lst = []
    for i in range(a-1, b):
        lst.append(n_lst[i])

    m = max(lst)

    for i in range(len(n_lst)):
        if(m == n_lst[i]):
            return i+1

n = int(input())
n_lst = map(int, input().split())
n_lst = list(n_lst)

a, b = input().split()
a = int(a)
b = int(b)

print(maxi(a, b))