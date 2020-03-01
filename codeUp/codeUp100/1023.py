'''
1023 : [기초-입출력] 실수 1개 입력받아 부분별로 출력하기(설명)

실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
첫 번째 줄에 정수 부분을, 두 번째 줄에 실수 부분을 출력한다.

INPUT
1.414213

OUTPUT
1
414213
'''
myInt, myFloat = input().split('.')
print(int(myInt))
print(int(myFloat))

