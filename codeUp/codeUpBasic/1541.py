'''
1541 : [기초-함수작성] 함수로 negative/zero/positive 출력하기
음수(-) 가 입력되면 negative, 0 이 입력되면 zero, 그 외에는 positive 를 출력한다.
'''
def f(n):
    if(n>0):
        print("positive")
    elif(n==0):
        print("zero")
    else:
        print("negative")

n = int(input())
f(n)