'''
1411 : 빠진 카드
우리는 1부터 N까지의 숫자가 차례대로 적힌 N장의 카드 묶음을 가지고 있다.
그런 데 이 카드 묶음을 옮기는 중 실수로 땅에 떨어뜨려 그 중 한 장을 잃어버렸다.
여러 분은 땅에 떨어진 카드 묶음을 읽어서 빠진 하나의 카드 번호를 찾아 출력해야 한다.
'''
# 잃어버리기 전 카드의 장 수
n = int(input())
mylist = []

# 현재 가지고 있는 카드의 번호
for i in range(n-1):
    num = int(input())
    mylist.append(num)

# 원래 있어야하는 카드 리스트
card_list = [x for x in range(1, n+1)]
card_list = set(card_list)

# 현재 리스트 set으로 변경
mylist = set(mylist)

lost_num = card_list-mylist
lost_num = list(lost_num)
print(lost_num[0])