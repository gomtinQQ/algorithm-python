'''
1577 : (함수 작성) 절댓값 함수 1
이 문제는 절댓값 함수를 구현하는 문제입니다.
다음 조건을 참고해서 함수 본체만 작성해서 제출하시기 바랍니다.
함수명 : myabs
매개 변수(parameter) :정수형(int) 1개
반환 형(return type) : 정수형(int)
함수 내용 : 절댓값을 구하는 함수 구현
'''
def myabs(x):
    return abs(x)

x = int(input())
print(myabs(x))