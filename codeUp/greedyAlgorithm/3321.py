'''
3321 : 최고의 피자
 피자 가게에서 주문할 수 있는 피자 중 1 달러 당 열량이 최대가 되는 피자를 주문하고 싶어한다.
Miss 피자는 N 종류의 토핑에서 여러 종류를 자유롭게 선택하여, 도우 위에 올려 주문할 수있다.
같은 토핑을 2 개 이상 올릴 수 없다.
도우에 토핑을 하나도 하지 않은  피자도 주문할 수있다.
도우의 가격은 A 달러이며, 토핑의 가격은 모두 B 달러이다.
실제 피자 가격은 도우의 가격과 토핑 가격의 합계이다.
즉, 토핑을 k 종류 (0 ≦ k ≦ N) 한 피자의 가격은 A + k × B 원이다.
피자 전체의 칼로리는 도우 열량과 토핑 칼로리의 합계이다.
도우의 가격과 토핑의 가격, 그리고 도우와 각 토핑 열량 값이 주어 졌을 때, "최고의 피자"의 1 달러 당 열량의 수를 구하는 프로그램을 작성하시오.


첫 번째 줄에는 토핑 종류 수를 나타내는 하나의 정수 N (1 ≦ N ≦ 100)이 입력된다.
두 번째 줄에는 두 개의 정수 A, B (1 ≦ A ≦ 1000,1 ≦ B ≦ 1000)가 공백을 구분으로 입력된다. A는 도우의 가격, B는 토핑의 가격을 나타낸다.
세 번째 줄에는 도우의 칼로리를 나타내는 정수 C (1 ≦ C ≦ 10000)가 입력된다.
3 + i 행 (1 ≦ i ≦ N)는 i 번째의 토핑 칼로리 수를 나타내는 정수 Di (1 ≦ Di ≦ 10,000)가 입력된다.

3 # 토핑 종류 수
12 2 # 도우의 가격/ 토핑 가격
200 # 도우의 칼로리
50 # 토핑 1
300 # 토핑 2
100 # 토핑 3
'''
numberOfTopping = int(input()) # 토핑 종류 수 
doughPrice, toppingPrice = input().split() # 도우의 가격/토핑 가격
doughKcal = int(input()) # 도우의 칼로리
toppingList = [] # 토핑
for i in range(numberOfTopping):
    toppingList.append(int(input()))

toppingList = sorted(toppingList, reverse=True) # 열량이 큰 토핑순으로 정렬
doughPrice = int(doughPrice)
toppingPrice = int(toppingPrice)

kcal = doughKcal
price = doughPrice
result = kcal/price

for i in toppingList:
    if result >= (kcal+i)/(price+toppingPrice):
        break
    else:
        kcal = kcal + i
        price += toppingPrice
        result = kcal/price

print(int(result))


