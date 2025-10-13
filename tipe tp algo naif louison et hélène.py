#https://fr.doczz.net/doc/3595989/tp---algorithmes-de-backtracking-et-r%C3%A9solution-de-sudoku
L=[[0, 9, 0, 2, 0, 0, 6, 0, 5], [3, 2, 0,0, 0, 7, 0, 0, 0], [0, 7, 0, 9, 0, 5, 0, 0,8], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 7,0, 0, 0, 0, 9, 4], [6, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 8, 0, 0, 0, 0, 0, 7], [0, 3, 0,4, 9, 1, 5, 0, 0], [0, 0, 0, 0, 0, 3, 0, 0,0]]

def chiffreligne(L, i):
    l = []
    for j in L[i]:
        if j != 0:
            l.append(j)
    return l

def chiffrecolonnes(L,j):
    l=[]
    for k in range (len(L[0])):
        if L[k][j] != 0:
            l.append(L[k][j])
    return l

def chiffrebloc(L,i,j):
    l=[]
    departi=i-i%3
    departj=j-j%3
    for k in range (departi,departi +3):
        for p in range (departj, departj +3):
            if L[k][p]!=0:
                l.append (L[k][p])
    return l

def chiffreconflit(L,i,j):
    l1=chiffreligne(L,i)
    l2=chiffrecolonnes(L,j)
    l3=chiffrebloc(L,i,j)
    return l1+l2+l3

def casesuivante (i,j):
    if j ==8 : return i+1,0
    return i,j+1
        

def solution(L):
    def aux (i,j):
        if i == 9 and j == 0:
            return True
        else:
            if L[i][j]!=0:
               aux(casesuivante(i,j))
            l=[ k for k in range (1,10) if k not in chiffreconflit(L,i,j)]
            for e in l:


