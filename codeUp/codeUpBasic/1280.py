'''
1280 : 홀수는 더하고 짝수는 빼고 2
두 자연수 a, b 사이의 구간에 대해서
홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.
단, 결과가 양수이면 +를 붙이지 않는다.
예)
a = 5, b=10 일 경우, +5-6+7-8+9-10=-3
a = 6, b=9 일 경우, -6+7-8+9=2
'''
a, b = input().split()
a = int(a)
b = int(b)
num_list = []
sum = 0

for i in range(a, b+1):
    if(i%2==0):
        num_list.append("-{0}".format(i))
        sum -= i
    else:
        num_list.append("+{0}".format(i))
        sum += i

for i in range(len(num_list)):
    print(num_list[i], end="")
print("={0}".format(sum))