'''
문제: [1차] 비밀지도
'''
def solution(n, arr1, arr2):
    map1 = [list(map(int, bin(i)[2:].zfill(n))) for i in arr1]
    map2 = [list(map(int, bin(i)[2:].zfill(n))) for i in arr2]
    result = []

    for i in range(n):
        tmp = [map1[i][j] or map2[i][j] for j in range(n)]
        tmp2 = ["#" if i == 1 else " " for i in tmp]
        result.append(''.join(tmp2))

    return result