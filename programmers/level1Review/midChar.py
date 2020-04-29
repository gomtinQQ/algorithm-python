'''
문제: 가운데 글자 가져오기
'''
def solution(s):
    slen = len(s)
    if slen%2==0:
        return s[int(slen / 2) - 1:int(slen / 2) +1]
    else:
        return s[int(slen / 2)]

print(solution("abcde"))
print(solution("qwer"))