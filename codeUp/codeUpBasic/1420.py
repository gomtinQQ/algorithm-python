'''
n명의 친구들의 이름과 정보 성적이 주어졌을 때 성적이 세 번째로 높은 학생의 이름을 출력하시오.
'''
n = int(input())
mydict = {}

for i in range(n):
    name, score = input().split()
    mydict[name] = int(score)

result = sorted(mydict.items(), key=lambda t:t[1], reverse=True)
print(result[2][0])

