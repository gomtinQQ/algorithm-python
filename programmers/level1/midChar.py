'''
문제: 가운데 글자 가져오기

문제 설명:
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

제한 사항:
1) s는 길이가 1 이상, 100이하인 스트링입니다.
'''
def solution(s):
    if (len(s) % 2 == 0):
        mid = int(len(s) / 2)
        return s[mid - 1:mid + 1]
    else:
        mid = int(len(s) / 2)
        return s[mid]

s = input()
print(solution(s))
