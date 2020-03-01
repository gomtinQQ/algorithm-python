'''
1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)

다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
다섯 자리로 이루어진 1개의 정수를 입력받는다.
(단, 10,000 <= 입력받는 수 <= 99,999 )

각 자리의 숫자를 분리해 한 줄에 하나씩 [ ]속에 넣어 출력한다.

INPUT
75254

OUTPUT
[70000]
[5000]
[200]
[50]
[4]
'''
myNumber = input()
myNumberList = list(myNumber)

print("[" + str(int(myNumberList[0])*10000) + "]")
print("[" + str(int(myNumberList[1])*1000) + "]")
print("[" + str(int(myNumberList[2])*100) + "]")
print("[" + str(int(myNumberList[3])*10) + "]")
print("[" + str(int(myNumberList[4])) + "]")