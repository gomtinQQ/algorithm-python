'''
1284 : 암호 해독
이에 대비해 어떤 수(n)가 입력되면 두 소수의 곱으로 나타낼 수 있으면 두 소수를 오름차순으로 출력하고,
그렇지 않으면 "wrong number"를 출력하는 프로그램을 작성하시오.
'''

# 최대공약수 구하기
def gcd (n):
    gcd_list = []
    for i in range(1, n+1):
        if(n%i==0):
            if(i> int(n/i)):
                gcd_list.append((int(n/i), i))
            else:
                gcd_list.append((i, int(n/i)))
    return gcd_list

# 소수인지 확인하기
def prime(list):
    prime_list = []
    cnt = 0
    for i in range(len(list)):
        if(1 in list[i]):
            continue
        elif((list[i][0]%2!=0 and list[i][0]%3!=0) or list[i][0]==2 or list[i][0]==3):
            if((list[i][1]%2!=0 and list[i][1]%3!=0) or list[i][1]==2 or list[i][1]==3):
                prime_list.append(list[i])
                cnt += 1
    return prime_list, cnt

n = int(input())

num_list = gcd(n)

# 리스트 내에서 중복 제거
gcd_list = set(num_list)
gcd_list = list(gcd_list)

# 소수 확인
prime_list, cnt = prime(gcd_list)
if(2 > cnt >= 1):
    for i in range(len(prime_list)):
        print(prime_list[i][0], prime_list[i][1])
else:
    print("wrong number")
