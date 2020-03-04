'''
1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기(설명)
정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''
x = int(input())
if(x>0):
    print("plus")
    if(x%2==0):
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if(x%2==0):
        print("even")
    else:
        print("odd")
