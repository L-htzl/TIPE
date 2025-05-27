#import sys
import numpy as np
#sys.path.append('C:\\Users\\vlixi\\AppData\\Roaming\\Python\\Python311\\site-packages')

from pysat.formula import CNF
from pysat.solvers import Solver

def sudoku(conditions):
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

    #def init():
     #   return(au_moins_un_cfr()+au_plus_un_cfr()+r_ts_cfr()+c_ts_cfr()+box_ts_cfr()+conditions)

    clauses=au_moins_un_cfr()+au_plus_un_cfr()+r_ts_cfr()+c_ts_cfr()+box_ts_cfr()+conditions
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
    #print(c)
    #print(bad_res)


    def nbr_a_cfr(x):
        a=x//100
        b=(x-a*100)//10
        c=(x-b*10-a*100)
        return (a,b,c)

    def affiche(cnf):
        M=np.zeros((9,9),dtype=int)
        for i in cnf :
            (a,b,c)=nbr_a_cfr(i)
            M[a-1,b-1]=c
        return M

    print(affiche(bad_res))

##

sudoku([[122],[133],[179],[211],[244],[255],[288],[366],[377],[424],[435],[516],[547],[559],[568],[591],[673],[682],[738],[742],[829],[851],[863],[895],[937],[974],[986]])
