'''
1602 : 절대값 함수
절대값 함수를 만들어 봅시다.
입력으로 정수가 들어오면 정수로 결과를 출력하고, 실수가 들어오면 실수로 결과를 출력한다.
단, 소수점 이하에 불필요한 0은 입력되지 않는다.
'''
def myabs(n):
    if(n.count('.')==1):
        return abs(float(n))
    else:
        return abs(int(n))

n = input()
print(myabs(n))