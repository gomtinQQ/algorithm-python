'''
1358 : 삼각형 출력하기 5
어떤 수 n을 입력받으면 다음과 같은 삼각형을 출력한다.
여기서 입력되는 n은 반드시 홀수이다.
'''
n = int(input())
for i in range(1, n+1):
    if(i%2!=0):
        for j in range(int((n-i)/2)):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()