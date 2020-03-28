'''
1418 : t를 찾아라
어떤 문자열이 있을 때 문자 t의 위치를 모두 찾아 출력하시오.
'''
mystring = input()
for i in range(0, len(mystring)):
    if(mystring[i]=='t'):
        print(i+1, end=" ")

