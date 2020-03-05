'''
1부터 n까지, 1부터 m까지 숫자가 적힌
서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.
주사위 2개의 면의 개수 n, m이 공백을 두고 입력된다.
단, n, m은 10이하의 자연수
'''
n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    i = i+1
    for j in range(m):
        j = j+1
        print(i ,j)
