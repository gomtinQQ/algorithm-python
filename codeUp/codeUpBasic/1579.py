'''
1579 : (함수 작성) 최솟값 함수
함수명 : mymin
매개 변수(parameter) :정수형(int) 2개
반환 형(return type) : 정수형(int)
함수 내용 : 두 정수 중 작은 값을 구하는 함수 구현
'''
def mymin(x,y):
    if(x > y):
        return y
    else:
        return x

x, y = input().split()
x = int(x)
y = int(y)
print(mymin(x,y))