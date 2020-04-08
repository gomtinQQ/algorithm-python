'''
1929 : (재귀함수) 우박수 (3n+1) (reverse)

콜라츠의 추측, 3n+1 문제, 우박수 문제라고 불리는 이 문제는 다음과 같다.

1, 어떤 자연수 n이 입력되면,
2. n이 홀수이면 3n+1을 하고,
3. n이 짝수이면 n/2를 한다.
4. 이 n이 1이 될때까지 2 3과정을 반복한다.
예를 들어 5는 5 → 16 → 8 → 4 → 2 → 1 이 된다.
그런데 이번에는 이 순서의 역순을 출력하고자 한다.
즉, 1 2 4 8 16 5 가 출력되어야 한다.
이 처럼 어떤 자연수 n이 입력되면 위 알고리즘에 의해 1이 되는 과정을 모두 출력하시오.
이 문제는 반복문 for, while 등을 이용하여 풀수 없습니다.
'''
def f(n):
    if(n==1):
        print(n)
        return
    elif(n%2==0):
        f(int(n/2))

    else:
        f(3*n+1)
    print(n)

n = int(input())
f(n)