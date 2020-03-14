'''
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

참고
가로 번호, 세로 번호를 사용할 수 있는 2차원 배열을 사용하면
이러한 형태를 쉽게 기록하고 사용할 수 있다. 물론 더 확장한 n차원 배열도 만들 수 있다.

INPUT : 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

OUTPUT: 십자 뒤집기 결과를 출력한다.

'''
#STEP1: 19X19 바둑판을 만든다.
MAX_VALUE = 19
checkerBoard = [[0 for i in range(MAX_VALUE)] for j in range(MAX_VALUE)]

#STEP2: 입력 값을 받는다.
for i in range(MAX_VALUE):
    temp = list(map(int, input().split()))
    for j in range(MAX_VALUE):
        checkerBoard[i][j] = temp[j]

#STEP3: 좌표 개수 입력 받기.
n = int(input())

#STEP4: 좌표 개수 만큼 흑/백 바꾸기
for i in range(n):
    x,y = map(int, input().split())

    #STEP5: 가로줄 흑/백 바꾸기
    for k in range(MAX_VALUE):
        #흰 돌 -> 검은 돌
        if checkerBoard[x-1][k]==1:
            checkerBoard[x-1][k]=0
        #검은 돌 -> 흰 돌
        elif checkerBoard[x-1][k]==0:
            checkerBoard[x-1][k]=1

    #STEP6: 세로줄 흑/백 바꾸기
    for k in range(MAX_VALUE):
        #흰 돌 -> 검은 돌
        if checkerBoard[k][y-1]==1:
            checkerBoard[k][y-1]=0
        #검은 돌 -> 흰 돌
        elif checkerBoard[k][y-1]==0:
            checkerBoard[k][y-1]=1
#STEP7: 바둑판 출력
for i in range(MAX_VALUE):
    for j in range(MAX_VALUE):
        print(checkerBoard[i][j], end=' ')
    print(end='\n')
