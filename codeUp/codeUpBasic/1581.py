'''
1581 : (함수 작성+포인터) swap 함수 만들기 (Call by Reference)
함수명 : myswap
매개 변수(parameter) : 정수형 포인터 변수 변수 2개(매개변수를 반드시 int∗로 사용)
반환 형(return type) : 없음(void)
함수 내용 : 첫 번째 포인터가 가리키는 변수의 값이 두 번째 포인터가 가리키는 변수의 값보다 클 경우 두 값을 서로 바꾼다.
'''
def myswap(a, b):
    tmp = 0
    if(a > b):
        tmp = a
        a = b
        b = tmp
    print(a, b)

a, b = input().split()
a = int(a)
b = int(b)
myswap(a, b)
