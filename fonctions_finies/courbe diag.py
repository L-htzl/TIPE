

#algo sat

import copy
import numpy as np
import time
from pysat.formula import CNF
from pysat.solvers import Solver
import random 
import matplotlib.pyplot as plt


conditions =[[122],[133],[179],[211],[244],[255],[288],[366],[377],[424],[435],[516],[547],[559],[568],[591],[673],[682],[738],[742],[829],[851],[863],[895],[937],[974],[986]]
conditions2 =[[122],[133],[179],[211],[244],[255],[288],[366],[377],[424],[435],[516],[547],[559],[568],[591],[673],[682],[738],[742],[829],[851],[863],[895]]

def tsf(i,j,n):
    ''' à un triplet (i,j,n) = (ligne,colonne, chiffre) associe un nombre unique correspondant -> fonction bijective '''
    return int(str(i)+str(j)+str(n))

def au_moins_un_cfr():
    ''' every cell contains at least one number'''
    C1=[]
    for i in range (1,10):
        for j in range (1,10):
            l=[]
            for n in range (1,10):
                l.append(tsf(i,j,n))
            C1.append(l)
    return C1

def au_plus_un_cfr():
    C2=[]
    for i in range(1,10):
        for j in range(1,10):
            for x in range(1,9):
                for y in range(x+1,10):
                    C2.append([-tsf(i,j,x),-tsf(i,j,y)])
    return C2




def r_ts_cfr():
    '''every row contains every number'''
    C3=[]
    for i in range (1,10):
        for n in range (1,10):
            l=[]
            for j in range (1,10):
                l.append(tsf(i,j,n))
            C3.append(l)
    return C3

def c_ts_cfr():
    '''every column contains every number'''
    C4=[]
    for j in range (1,10):
        for n in range (1,10):
            l=[]
            for i in range (1,10):
                l.append(tsf(i,j,n))
            C4.append(l)
    return C4


def box_ts_cfr():
    ''' every 3x3 box contains every number '''
    C5=[]
    for r in range(3):
        for s in range(3):
            for n in range (1,10):
                l=[]
                for i in range (1,4):
                    for j in range (1,4):
                        l.append(tsf(3*r+i,3*s+j,n))
                C5.append(l)
    return C5

def diag_pr_au_moins_un_cfr():
    '''chaque chiffre apparait au moins une fois sur la diagonale principale i=j'''
    c=[]
    for k in range (1,10):
        l=[]
        for i in range (1,10):
            l.append(tsf(i,i,k))
        c.append(l)
    return c 

def diag_pr_au_plus_un_cfr():
    '''chaque chiffre apparait au plus une fois sur la diagonale principale i=j'''
    c=[]
    for k in range (1,10):
        for i in range (1,9):
            for j in range (i+1,10):
                c.append([-tsf(i,i,k),-tsf(j,j,k)])
    return c 

def diag_sc_au_moins_un_cfr():
    '''chaque chiffre apparait au moins une fois sur la diagonale secondaire  i+j = 10'''
    c=[]
    for k in range (1,10):
        l=[]
        for i in range (1,10):
            l.append(tsf(i,10-i,k))
        c.append(l)
    return c 
    
def diag_sc_au_plus_un_cfr():
    '''chaque chiffre apparait au plus une fois sur la diagonale secondaire i+j = 10 '''
    c=[]
    for k in range (1,10):
        for i in range (1,9):
            for j in range (i+1,10):
                c.append([-tsf(i,10-i,k),-tsf(j,10-j,k)])
    return c     
def pas_la_mm_sol(cnf):
    l=[-x for x in cnf]
    return [l]    
    
conditions_sudoku = diag_sc_au_plus_un_cfr()+diag_sc_au_moins_un_cfr()+diag_pr_au_plus_un_cfr()+diag_pr_au_moins_un_cfr()+au_moins_un_cfr()+au_plus_un_cfr()+r_ts_cfr()+c_ts_cfr()+box_ts_cfr()


# def nbr_a_cfr(x):
#     a=x//100
#     b=(x-a*100)//10
#     c=(x-b*10-a*100)
#     return (a,b,c)

def affiche(cnf):
    M=np.zeros((9,9),dtype=int)
    for i in cnf :
        (a,b,c)=nbr_a_cfr(i)
        M[a-1,b-1]=c
    return M

def sudoku(conditions=[]):
    
    clauses= conditions_sudoku+conditions
    cnf=CNF(from_clauses=clauses)
    with Solver(bootstrap_with=cnf) as solver :
        if not solver.solve():
            return None
        #print(solver.solve())
        res=solver.get_model()
    return [x for x in res if x > 0]

def sudoku_cnf(conditions=[]):
    clauses=conditions_sudoku+conditions
    cnf=CNF(from_clauses=clauses)
    with Solver(bootstrap_with=cnf) as solver :
        sol=solver.solve()
        #print(solver.solve())
        res=solver.get_model()
    c=0
    bad_res=[]
    for x in res:
        if x>0:
            c+=1
            bad_res.append(x)
    return (bad_res)

# def unique_sol (conditions=[]):
#     if len(conditions)<17: return False
#     cnf=sudoku_cnf(conditions)
#     try:
#         sol=sudoku(conditions_sudoku+conditions+pas_la_mm_sol(cnf))
#         print(sol)
#         return False
#     except (TypeError,NameError):
#         return True

def unique_sol(conditions):
    sol1 = sudoku_cnf(conditions)
    if sol1 is None:
        return False
    sol2 = sudoku(conditions + pas_la_mm_sol(sol1))
    return sol2 is None
    
def toutes_sol (conditions =[]):
    print(sudoku(conditions))
    while unique_sol(conditions) == False :
        cnf=sudoku_cnf(conditions)
        conditions+= pas_la_mm_sol(cnf) 
        print(sudoku(conditions))
# algo naïf

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
        if i == 9 :
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

#courbes 

def cfr_a_nbr (a,b,c):
    return a*100+b*10+c

def nbr_a_cfr(x):
    a=x//100
    b=(x-a*100)//10
    c=(x-b*10-a*100)
    return (a,b,c)

def naif_a_sat (t):
    l=[]
    for i in range(9):
        for j in range(9):
            nbr=cfr_a_nbr(i+1,j+1,t[i][j])
            l.append([nbr])
    return l
            
# def retirer (l,e):
#     print(len(l))
#     i=0
#     while l[i]!=e and i<len(l):
#         i+=1
#         print(i)
#     return l[:i]+l[i+1:]

def retirer(l,e):
    for i in range(len(l)):
        if l[i]==e:
            return l[:i]+l[i+1:]
        
def temps_naif(sudokunaif):
    s=copy.deepcopy(sudokunaif)
    t0=time.time()
    s=solution(s)
    t1=time.time()
    return t1-t0

def temps_sat(sudokusat):
    t0=time.time()
    s=sudoku(sudokusat)
    t1=time.time()
    return t1-t0
    

def complexite (nbfinal):
    x=[i for i in range(0,81-nbfinal+1)]
    y_naif=[]
    y_sat=[]
    sudokunaif= [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [4, 5, 6, 7, 8, 9, 1, 2, 3],
     [7, 8, 9, 1, 2, 3, 4, 5, 6],
     [2, 1, 4, 3, 6, 5, 8, 9, 7],
     [3, 6, 8, 9, 7, 2, 5, 1, 4],
     [5, 9, 7, 8, 1, 4, 6, 3, 2],
     [9, 4, 1, 6, 3, 8, 2, 7, 5],
     [8, 3, 2, 5, 4, 7, 9, 6, 1],
     [6, 7, 5, 2, 9, 1, 3, 4, 8]]
    
    sudokusat=[[111],
     [122],
     [133],
     [144],
     [155],
     [166],
     [177],
     [188],
     [199],
     [214],
     [225],
     [236],
     [247],
     [258],
     [269],
     [271],
     [282],
     [293],
     [317],
     [328],
     [339],
     [341],
     [352],
     [363],
     [374],
     [385],
     [396],
     [412],
     [421],
     [434],
     [443],
     [456],
     [465],
     [478],
     [489],
     [497],
     [513],
     [526],
     [538],
     [549],
     [557],
     [562],
     [575],
     [581],
     [594],
     [615],
     [629],
     [637],
     [648],
     [651],
     [664],
     [676],
     [683],
     [692],
     [719],
     [724],
     [731],
     [746],
     [753],
     [768],
     [772],
     [787],
     [795],
     [818],
     [823],
     [832],
     [845],
     [854],
     [867],
     [879],
     [886],
     [891],
     [916],
     [927],
     [935],
     [942],
     [959],
     [961],
     [973],
     [984],
     [998]]

    y_naif.append(temps_naif(sudokunaif))
    y_sat.append(temps_sat(sudokusat))
    while len(sudokusat)> nbfinal:
        aleatoire = random.choice(sudokusat)
        (a,b,c) = nbr_a_cfr(aleatoire[0])
        sudokunaif[a-1][b-1]=0
        sudokusat=retirer(sudokusat,aleatoire)
        y_naif.append(temps_naif(sudokunaif))
        y_sat.append(temps_sat(sudokusat))
    plt.plot(x,y_naif,label='algo naïf', color='red')
    plt.plot(x,y_sat,label='algo sat', color='blue')
    plt.title('complexité')
    plt.xlabel("nombre d'inconnues")
    plt.ylabel("temps")
    plt.show()

        
