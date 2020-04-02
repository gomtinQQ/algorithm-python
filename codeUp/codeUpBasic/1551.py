'''
1551 : [기초-함수작성] 함수로 원하는 값의 위치 리턴하기 1
n 개의 정수를 배열로 입력 받고,
원하는 값 k가 저장되어있는 가장 처음 위치를 출력하시오.
(원하는 값 k값이 저장되어있지 않은 경우에는 –1을 출력한다.)
단, 함수형 문제이므로 함수 f()만 작성하시오.
'''
def f(lst, myNum):
    for i in range(len(lst)):
        lst[i]  = int(lst[i])

    for i in range(len(lst)):
        if (myNum == lst[i]):
            return i+1
        if (myNum not in lst):
            return -1

n = int(input())
lst = input().split()
myNum = int(input())

print(f(lst, myNum))