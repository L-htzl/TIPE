from random import * 
import matplotlib.pyplot as plt
import time

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
            
def retirer (l,e):
    i=0
    while l[i]!=e and i<len(l):
        i+=1
    l= l[:i-1]+l[i:]

def temps_naif(sudokunaif):
    t0=time.time()
    solution(sudokunaif)
    t1=time.time()
    return t1-t0

def temps_sat(sudokusat):
    t0=time.time()
    sudoku(sudokunaif)
    t1=time.time()
    return t1-t0
    

def complexite (nbfinal):
    x=[i for i in range(0,100)]
    y_naif=[]
    y_sat=[]
    sudokunaif= [[8, 9, 1, 2, 3, 4, 6, 7, 5],
     [3, 2, 5, 6, 8, 7, 4, 1, 9],
     [4, 7, 6, 9, 1, 5, 3, 2, 8],
     [9, 1, 4, 7, 5, 2, 8, 6, 3],
     [2, 5, 7, 3, 6, 8, 1, 9, 4],
     [6, 8, 3, 1, 4, 9, 7, 5, 2],
     [1, 4, 8, 5, 2, 6, 9, 3, 7],
     [7, 3, 2, 4, 9, 1, 5, 8, 6],
     [5, 6, 9, 8, 7, 3, 2, 4, 1]]
    sudokusat=[[118],[129],[131],[142],[153],[164],[176],[187],[195],[213],[222],[235],[246],[258],[267],[274],[281],[299],[314],[327],[336],[349],[351],[365],[373],[382],[398],[419],[421],[434],[447],[455],[462],[478],[486],[493],[512],[525],[537],[543],[556],[568],[571],[589],[594],[616],[628],[633],[641],[654],[669],[677],[685],[692],[711],[724],[738],[745],[752],[766],[779],[783],[797],[817],[823],[832],[844],[859],[861],[875],[888],[896],[915],[926],[939],[948],[957],[963],[972],[984],[991]]
    y_naif.append(temps_naif(sudokunaif))
    y_sat.append(temps_sat(sudokusat))
    
    while len(sudokusat)> nbfinal:
        aleatoire = random.randint(1,999)
        (a,b,c) = nbr_a_cfr(aleatoire)
        sudokunaif[a][b]=0
        retirer(sudokusat,aleatoire)
        y_naif.append(temps_naif(sudokunaif))
        y_sat.append(temps_sat(sudokusat))
    plt.plot(x,y_naif,label='algo naïf')
    plt.plot(x,y_sat,label='algo sat')
    plt.title('complexité')
    plt.xlabel("nombre d'inconnues")
    plt.ylabel("temps")
    plt.show()
        
               
        

        
