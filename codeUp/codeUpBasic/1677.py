'''
1677 : 종이 만들기
n*m 종이를 만들려고 한다.
가로 길이와 세로 길이가 주어지면 다음과 같은 종이를 출력하시오.
예를 들어) 4 * 3의 종이라면
+--+
|  |
+--+
이와 같이 출력한다.
'''
n, m = input().split()
n = int(n)
m = int(m)

for i in range(m):
    if(i==0 or i==(m-1)):
        for j in range(n):
            if(j==0 or j==(n-1)):
                print("+", end="")
            else:
                print("-", end="")
    else:
        for j in range(n):
            if(j==0 or j==(n-1)):
                print("|", end="")
            else:
                print(" ", end="")

    print()