'''
1578 : (함수 작성) 최댓값 함수
함수명 : mymax
매개 변수(parameter) :정수형(int) 2개
반환 형(return type) : 정수형(int)
함수 내용 : 두 정수 중 큰 값을 구하는 함수 구현
'''
def mymax(x, y):
    if(x > y):
        return x
    else:
        return y

x, y = input().split()
x = int(x)
y = int(y)
print(mymax(x,y))