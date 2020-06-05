'''
문제: [1차] 다트게임
'''
import re
def solution(dartResult):
    p = re.compile('([0-9]{1,2})([A-Z])([*#])?')
    dartScore = p.findall(dartResult)
    s = []
    result = []
    # (10, S, *)
    for i in range(len(dartScore)):
        s.append(dartScore[i][0])
        s.append(dartScore[i][1])
        if dartScore[i][2] != '':
            s.append(dartScore[i][2])

    while s:
        x = s.pop(0)
        if x.isdigit():
            result.append(int(x))
        elif x == 'D':
            tmp = result.pop()
            result.append(tmp ** 2)
        elif x == 'T':
            tmp = result.pop()
            result.append(tmp ** 3)
        elif x == '*':
            if len(result) == 1:
                tmp = result.pop()
                result.append(tmp * 2)
            else:
                tmp1, tmp2 = result.pop(), result.pop()
                result.append(tmp2 * 2)
                result.append(tmp1 * 2)
        elif x == '#':
            tmp = result.pop()
            result.append(tmp * (-1))
    return (sum(result))