'''
1440 : 비교
5
1 2 3 2 1

1: < < < =
2: > < = >
3: > > > >
4: > = < >
5: = < < <
'''
n = int(input())
n_list = input().split()

for i in range(n):
    print("{0}:".format(i+1), end=" ")

    for j in range(n):
        if(j==i):
            continue
        elif(int(n_list[i]) > int(n_list[j])):
            print(">", end=" ")
        elif(int(n_list[i]) < int(n_list[j])):
            print("<", end=" ")
        else:
            print("=", end=" ")

    print()


