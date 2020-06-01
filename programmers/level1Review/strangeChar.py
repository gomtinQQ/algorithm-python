'''
문제: 이상한 문자 만들기
'''
s = "try hello world"
stringArr = list(s.split(" "))
charList = [[mychar[i].upper() if i%2==0 else mychar[i].lower() for i in range(len(mychar))] for mychar in stringArr]
result = ' '.join([''.join(s) for s in charList])
print(result)
