'''
문제: 비밀지도

문제 설명:
1. 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류로 이루어져 있다.
2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 지도 1과 지도 2라고 하자.
지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
3. 지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다.
4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

5
9 20 28 18 11
30 1 21 17 28
'''

n = int(input())
arr1 = input().split()
arr2 = input().split()
map1 = []
map2 = []
result = []

for i in arr1:
    tmp = bin(int(i))[2:]
    map1.append(list(tmp.zfill(n)))

for i in arr2:
    tmp = bin(int(i))[2:]
    map2.append(list(tmp.zfill(n)))

for i in range(0, n):
    tmp = []
    for j in range(0, n):
        x = int(map1[i][j]) + int(map2[i][j])
        if x > 0:
            tmp.append("#")
        else:
            tmp.append(" ")
    result.append(''.join(tmp))

print(result)