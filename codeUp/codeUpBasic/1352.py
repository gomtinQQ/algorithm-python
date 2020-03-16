'''
기초4-2. 중첩 반복문
1352 : 사각형 출력하기 1

길이 n이 입력되면 길이가 n인 사각형을 출력하시오.
단, 사각형은 * 모양으로 채운다.
'''

n = int(input())
for i in range(n):
    for i in range(n):
        print("*", end="")
    print(" ")
