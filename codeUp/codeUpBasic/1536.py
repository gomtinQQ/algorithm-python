'''
1536 : [기초-함수작성] 함수로 가장 작은 값 리턴하기
배열에서 가장 작은 값을 출력하시오.
단, 함수형 문제이므로 함수 f()만 작성하시오.
'''
def f(lst):
    m = min(lst)
    return m

n = int(input())
lst = list(map(int, input().split()))

print(f(lst))