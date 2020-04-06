'''
1615 : 셀프 넘버(Self-Number)
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어 d(91) = 9 + 1 + 91 = 101 이 때, n을 d(n)의 제네레이터(generator)라고 한다.
위의 예에서 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
시작 값(a)과 마지막 값(b)가 입력되면 두 수 사이의 셀프 넘버들의 합을 출력하시오.
'''
def self_number(a, b):
    lst = []
    # 1-5000까지 셀프 넘버를 lst에 넣는다.
    for i in range(1, 5001):
        lst.append(i + sum([int(j) for j in str(i)]))
    return sum(set(range(a, b+1)) - set(lst))

a, b = input().split()
a = int(a)
b = int(b)
print(self_number(a, b))
