'''
1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)
월 : 계절 이름
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
'''

def season(x):
    return{'12':'winter','1':'winter', '2':'winter',
           '3':'spring','4':'spring', '5':'spring',
           '6':'summer','7':'summer', '8':'summer',
           '9':'fall','10':'fall', '11':'fall'}

x = str(input())
print(season(x))