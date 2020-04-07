'''
1912 : (재귀함수) 팩토리얼 계산
팩토리얼(!)은 다음과 같이 정의된다.
n!=n×(n−1)×(n−2)×⋯×2×1
즉, 5!=5×4×3×2×1=120 이다.
n이 입력되면 n!의 값을 출력하시오.
'''
def f(n):
    global result
    global cnt

    if(cnt<=n):
        result *= cnt
        cnt = cnt+1
        f(n)
    return result

n = int(input())
result = 1
cnt = 1
print(f(n))