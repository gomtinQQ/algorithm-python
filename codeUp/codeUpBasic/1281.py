'''
1281 : 홀수는 더하고 짝수는 빼고 3
두 자연수 a, b 사이의 구간에 대해서
홀수는 더하고 짝수는 빼는 식을 보여준 후 결과를 출력하시오.
예)
a = 5, b=10 일 경우, 5-6+7-8+9-10=-3
a = 6, b=9 일 경우, -6+7-8+9=+2
'''
a, b = input().split()
a = int(a)
b = int(b)
sum = 0
num_list = []

for i in range(a, b+1):
    if(i%2!=0 and i==a):
        num_list.append("{0}".format(i))
        sum += i
    elif(i%2==0):
        num_list.append("-{0}".format(i))
        sum -= i
    else:
        num_list.append("+{0}".format(i))
        sum += i

for i in range(len(num_list)):
    print(num_list[i], end="")

if(sum>0):
    print("=+{0}".format(sum))
else:
    print("={0}".format(sum))