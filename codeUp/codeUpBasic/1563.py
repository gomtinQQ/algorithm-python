'''
1563 : [기초-함수작성] 함수로 세 정수 중 중간 값 리턴하기
int 형 정수 세 개를 입력 받아
중간 값을 출력하시오.
단, 함수형 문제이므로 함수 mid()만 작성하여 제출하시오.
'''
def mid(x, y, z):
    lst = [x,y,z]
    maxNum = max(lst)
    minNum = min(lst)
    sumNum = sum(lst)
    return sumNum-maxNum-minNum

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

print(mid(x,y,z))