'''
1542 : [기초-함수작성] 함수로 prime 또는 composite 출력하기
소수(prime)가 입력되면 prime, 합성수(composite)가 입력되면 composite 를 출력한다.
int 형 자연수(n)가 입력된다.
(2 <= n <= 1000)
'''
def f(n):
    if(n!=2 and (n%2==0 or n%3==0)):
        print("composite")
    else:
        print("prime")

n = int(input())
f(n)