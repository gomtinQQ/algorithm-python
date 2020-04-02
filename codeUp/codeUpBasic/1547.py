'''
1보다 큰 자연수 1개를 입력 받아
소수인 경우 prime, 합성수인 경우 composite를 출력하시오.
단, 함수형 문제이므로 함수 prime()만 제출하시오.
'''
def prime(n):
    cnt = 0
    for i in range(1, n+1):
        if(n%i==0):
            cnt+=1

    if(cnt>2):
        print("composite")
    else:
        print("prime")

n = int(input())
prime(n)