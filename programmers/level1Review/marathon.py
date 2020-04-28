'''
문제: 완주하지 못한 선수
'''
from collections import Counter
def solution(participant, completion):
    answer = [k for k, v in (Counter(participant) - Counter(completion)).items()]
    return ''.join(answer)

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))