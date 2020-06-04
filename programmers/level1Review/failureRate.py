'''
문제: 실패율
'''
def solution(N, stages):
    users = len(stages)
    stay = [stages.count(i) for i in range(1, N + 2)]
    clear = [sum(stay[i + 1:len(stay) + 1]) for i in range(len(stay) - 1)]
    # failure = [stay[i]/(stay[i]+clear[i]) for i in range(N)]
    failure = []
    for i in range(len(clear)):
        if clear[i] == 0 and stay[i] == 0:
            failure.append(0)
        else:
            failure.append(stay[i] / (stay[i] + clear[i]))

    result = []
    for i, f in enumerate(failure):
        result.append((i + 1, f))

    result.sort(key=lambda x: x[1], reverse=True)
    result = [i[0] for i in result]
    return result
