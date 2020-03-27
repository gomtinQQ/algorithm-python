'''
1425 : 자리 배치
왼쪽 위부터 차례대로 키 순서대로 앉으며 한 줄이 다 찼을 경우 다음 줄로 넘어간다. 다음 줄도 마찬가지로 왼쪽부터 채운다.
이와 같이 학생의 키순서대로 자리를 배치하는 프로그램을 작성하시오.
1. 첫 번째 줄에 학생 수(N)와 한줄에 앉을 수 있는 자리수(C)가 자연수로 주어진다. 단, (1≤N≤99), (1≤C≤10)
2. 둘째 줄에는 N명의 학생 키들이 공백으로 구분되어 입력된다.
'''
n, c = input().split()
students = input().split()
n = int(n)
c = int(c)

students = sorted(students)

for i in range(0, n):
    print(students[i], end=" ")
    if((i+1)%c==0):
        print()

