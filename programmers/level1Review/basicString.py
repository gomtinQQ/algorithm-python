'''
문제: 문자열 다루기 기
'''
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isnumeric():
            return True
    return False