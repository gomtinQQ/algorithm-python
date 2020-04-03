'''
1567 : [기초-함수작성] 함수로 배열의 부분합 리턴하기
배열의 참조 범위([a, b], a번부터 ~ b번까지 범위, 폐구간 [a, b])를 입력 받아
그 범위의 부분합을 출력하시오.
단, 함수형 문제이므로 함수 subsetsum()만 작성하여 제출하시오.
예를 들어 1 ~ n번으로 구성된 배열
1 5 3 4 2 에서
폐구간 [2, 4]의 부분합을 계산하면 5+3+4=12 가 된다.
'''
def subsetsum(a, b):
    sum = 0
    mylst = lst[a-1:b]
    for i in mylst:
        sum = sum + int(i)
    return sum

n = int(input())
lst = input().split()
a, b = input().split()
a = int(a)
b = int(b)
print(subsetsum(a, b))