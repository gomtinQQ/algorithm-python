'''
문제: 같은 숫자는 싫어
'''
def solution(arr):
    result = list()
    for i in arr:
        if len(result) == 0:
            result.append(i)
        if i != result[-1]:
            result.append(i)
    return result