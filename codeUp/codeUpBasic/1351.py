'''
기초4-2. 중첩 반복문
1351 : 구구단 출력하기 2

시작단과 마지막 단을 입력하면
그 구간의 구구단을 출력하는 프로그램을 작성하시오.
'''
x, y = input().split()
x = int(x)
y = int(y)

for i in range(x, y+1):
    for j in range(1, 10):
        print(str(i)+"*"+str(j)+"="+str(i*j))
