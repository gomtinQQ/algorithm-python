'''
1535 : [기초-함수작성] 함수로 가장 큰 값 위치 리턴하기
배열에서 가장 큰 값이 처음 나타나는 위치를 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성하시오.
'''
def f(lst):
    m = max(lst)
    for i in range(len(lst)):
        if(m==lst[i]):
            return i+1

n = int(input())
lst = input().split()

for i in range(n):
    lst[i] = int(lst[i])

print(f(lst))