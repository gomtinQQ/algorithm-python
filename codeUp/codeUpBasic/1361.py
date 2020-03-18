'''
1361 : 별 계단 만들기
n이 입력되면 n층의 별 계단을 출력하시오.

예) n= 5인 경우,
**
 **
  **
   **
    **
'''
n = int(input())
for i in range(1, n+1):
    print(" "*(i-1), end="")
    print("**")

