conditions = [[109],[215],[307],[403],[606],[808],[1013],[1202],[1416],[1512],[2010],[2207],[2313],[2405],[2601],[2914],[3015],
              [3102],[3209],[3305],[3712],[4110],[4208],[4307],[4713],[4801],[5011],[5101],[5410],[5602],[5705],[5915],[6009],
              [6107],[6304],[6508],[6716],[6805],[6901],[7004],[7213],[7502],[7715],[8014],[8207],[8411],[8616],[8706],[8915],
              [9010],[9103],[9301],[9405],[10214],[10410],[10708],[11012],[11103],[11216],[11515],[11705],[11803],[12104],[12301],
              [12506],[12611],[13016],[13208],[13306],[13607],[13809],[14014],[14103],[14315],[14410],[14511],[14613],[14712],[14909],
              [15001],[15105],[15516],[15906],[16106],[16503],[16608],[16710],[16901],[17002],[17112],[17215],[17316],[17505],
              [17613],[17810],[18113],[18215],[18304],[18416],[18508],[18806],[19001],[19307],[19408],[19511],[19616],[20006],
              [20310],[20401],[20714],[20815],[20915],[21103],[21204],[21516],[21712],[22008],[22105],[22407],[22514],[22809],
      
            [22907],[23112],[23203],[23506],[23708],[24011],[24201],[24310],[24412],[24613],[24714],[25207],[25406],[25603]]



def nbr_a_cfr(x):
    case = x // 100
    n = x % 100
    j = case % 16
    if j == 0:
        j = 16
    i = (case - j) // 16 + 1
    return (i, j, n)

def affiche(cnf):
    M=[[0 for _ in range (16)] for _ in range (16)]
    for i in cnf :
        (a,b,c)=nbr_a_cfr(i[0])
        M[a-1][b-1]=c
    return M

L=[[0 for _ in range (16)] for _ in range (16)]

def chiffrebloc(L,i,j):
    l=[]
    idepart=i-(i%4)
    jdepart=j-(j%4)
    for k in range(idepart,idepart+4):
        for m in range(jdepart,jdepart+4):
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

def chiffreconflit(L,i,j):
    impossible = chiffrebloc(L,i,j) + chiffreligne(L,i) + chiffrecolonnes(L,j)
    return impossible


def casesuivante(i,j):
    if j==14 : return i+1,0
    return i,j+1 
    
    
def solution(L):
    def aux (i,j):
        if i == 17 and j == 0:
            return True
        else:
            (a,b)=casesuivante(i,j)
            if L[i][j]!=0:
               return aux(a,b)
            l=[ k for k in range (1,17) if k not in chiffreconflit(L,i,j)]
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