'''
1580 : (함수 작성) 원의 넓이
함수명 : circle
매개 변수(parameter) :반지름(r)을 나타내는 정수형(int) 변수 1개
반환 형(return type) : 실수형(float)
함수 내용 : 원의 넓이를 구하는 함수 구현 (원의 넓이 = 3.14×r×r)
'''
def circle(r):
    return '%0.2f' %(3.14*r*r)

r = int(input())
print(circle(r))