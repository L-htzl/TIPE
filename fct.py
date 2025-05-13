from pysat.formula import CNF
from pysat.solvers import Solver

cnf=CNF(from_clauses=[[-1,2],[-1,-2]])

def tsf(i,j,n):
    ''' à un triplet (i,j,n) = (ligne,colonne, chiffre) associe un nombre unique correspondant -> fonction bijective '''
    return int(str(i)+str(j)+str(n))

def au_moins_un_cfr():
    ''' every cell contains at least one number'''
    C1=[[]for _ in range(9)]
    r=-1
    for i in range (1,10):
        r+=1
        for j in range (1,10):
            l=[]
            for n in range (1,10):
                l.append(tsf(i,j,n))
            C1[r].append(l)
    return C1

def r_ts_cfr():
    '''every row contains every number'''
    C3=[[]for _ in range(9)]
    r=-1
    for i in range (1,10):
        r+=1
        for n in range (1,10):
            l=[]
            for j in range (1,10):
                l.append(tsf(i,j,n))
            C3[r].append(l)
    return C3

def c_ts_cfr():
    '''every column contains every number'''
