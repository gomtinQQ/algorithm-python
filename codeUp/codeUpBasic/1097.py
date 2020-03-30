'''
1097 : [기초-2차원배열] 바둑알 십자 뒤집기(설명)
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
'''
chkbrd = []
x_lst = []
y_lst = []
# 바둑판 input
for i in range(19):
    chkbrd.append(input().split())

# 좌표 입력
n = int(input())
for i in range(n):
    x, y = input().split()
    x_lst.append(int(x))
    y_lst.append(int(y))

for i in range(n):
    x = x_lst[i]
    y = y_lst[i]
    # 가로 줄 흑, 백 바꾸기
    for j in range(19):
        if(chkbrd[x-1][j]=='1'):
            chkbrd[x-1][j] = '0'
        else:
            chkbrd[x - 1][j] = '1'
    # 세로 줄 흑, 백 바꾸기
    for j in range(19):
        if(chkbrd[j][y-1]=='1'):
            chkbrd[j][y-1] = '0'
        else:
            chkbrd[j][y-1] = '1'

for i in range(len(chkbrd)):
    for j in range(len(chkbrd)):
        print(chkbrd[i][j], end=" ")
    print()

