'''
문제: 크레인 인형뽑기 게임
'''

def solution(board, moves):
    stacklist = []
    cnt = 0

    for m in moves:
        for b in board:
            if (b[m - 1]) != 0:
                stacklist.append(b[m - 1])
                b[m - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop()
                        stacklist.pop()
                        cnt += 2
                break

    return cnt

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))