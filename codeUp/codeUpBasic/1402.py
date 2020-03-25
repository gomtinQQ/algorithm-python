'''
1402 : 거꾸로 출력하기 3
첫째 줄에 데이터의 개수 n이 입력된다. ( n <= 1,000 )
둘째 줄에 공백을 기준으로 n개 데이터가 입력된다.
n개의 데이터를 입력의 역순으로 출력한다.
'''
n = int(input())
list = input().split()
list.reverse()

for i in range(len(list)):
    print(list[i], end=" ")