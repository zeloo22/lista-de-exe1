def det(sist):
#função recebe um sistema n por n
    n=len(sist)
    m=len(sist[0])
    conttrocas=0
    for i in range(n-1):
        #varre vetor(coluna)
        while sist[i][i]==0:
           for t in range(m):
               troca=sist[t][i]
               sist[t][i]=sist[t][i+1]
               sist[t][i+1]=troca
               conttrocas+=1

    
        for j in range(i+1,n):
                #varre itens de linhas difwrentes de uma mesma coluna i)
            if sist[j][i]!=0:
                fator=sist[j][i]/sist[i][i]
                for k in range(m):
                    sist[j][k]=sist[j][k]-fator*sist[i][k]
        for x in range(n):
                    for y in range(m):
                        if sist[x][y]>0:
                            s='+'
                        elif sist[x][y]==0:
                            s=' '
                        else:
                            s=''
                        print(s+str(float(sist[x][y])), end=' ')
                    print()
        print()
                
    det=(-1)**conttrocas
    
    for diag in range(n):
        det*=sist[diag][diag]
    print("O determinante é {}".format(det))
    return det


matriz = [[3,-3,2,0,13], [-2,2,-2,-3,-7], [2,1,0,2,-2], [2,3,-3,-2,0]]
det(matriz)
