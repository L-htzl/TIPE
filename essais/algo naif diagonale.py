L=[[0, 9, 0, 2, 0, 0, 6, 0, 5], 
   [3, 2, 0,0, 0, 7, 0, 0, 0],
   [0, 7, 0, 9, 0, 5, 0, 0,8], 
   [0, 1, 0, 0, 0, 0, 0, 0, 0], 
   [0, 0, 7,0, 0, 0, 0, 9, 4], 
   [6, 0, 0, 0, 0, 0, 0, 0,0],
   [0, 0, 8, 0, 0, 0, 0, 0, 7],
   [0, 3, 0,4, 9, 1, 5, 0, 0],
   [0, 0, 0, 0, 0, 3, 0, 0,0]]
L2=[[0 for _ in range (9)]for _ in range (9)]
def chiffrebloc(L,i,j):
    l=[]
    idepart=i-(i%3)
    jdepart=j-(j%3)
    for k in range(idepart,idepart+3):
        for m in range(jdepart,jdepart+3):
            if L[k][m] != 0:
                l.append(L[k][m])
    return l
    
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


def chiffrediagonale(L):
    d=[]
    for k in range (len(L)):
        if L[k][k]!=0:
            d.append(L[k][k])
    return d

def chiffreantidiagonale(L):
    d=[]
    for k in range (len(L)):
        if L[k][len(L)-k-1] != 0 :
            d.append(L[k][len(L)-k-1])
    return d 
    

def chiffreconflit(L,i,j):
    impossible = chiffrebloc(L,i,j) + chiffreligne(L,i) + chiffrecolonnes(L,j) 
    if i==j:#dans la diagonale 
        impossible+= chiffrediagonale(L)
    if i+j==8: #dansl'antidiagonale
        impossible+=chiffreantidiagonale(L)
    return impossible
 

def casesuivante(i,j):
    if j==8 : return i+1,0
    return i,j+1 
    
    
def solution(L):
    def aux (i,j):
        if i == 9 and j == 0:
            return True
        else:
            (a,b)=casesuivante(i,j)
            if L[i][j]!=0:
               return aux(a,b)
            l=[ k for k in range (1,10) if k not in chiffreconflit(L,i,j)]
            if l==[] : return False
            e=0
            L[i][j]=l[e]
            while not aux(a,b):
                e+=1
                if e>= len(l):
                    L[i][j]=0
                    return False 
                L[i][j]=l[e]
            return True
    aux(0,0)
    return L


