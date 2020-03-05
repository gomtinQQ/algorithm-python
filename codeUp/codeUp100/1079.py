'''
1079 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
'''

list = input().split()
for c in list:
    print(c)
    if(c=='q'):
        break
