def pmat(m,ti,tj):
    for i in range(ti):
        for j in range(tj):
            print(m[i][j], end=" ")
        print()

#matrizcaio = [[1,2,-2,-1, 2, -1], [-2,-7,1,5,-1,8], [2,5,-4,-2,5,-6], [-1,-1,2,1,-1,-3], [2,2,-7,1,8,0], [-1,-1,1,2,1,-5]]
#matriz = [[3,2,-1,6], [-3,-4,4,-4], [-6,-10,13,-10]]
#matrizbia = [[1,2,-1,-1,-1,-1],[-2,-3,1,3,4,1],[2,2,0,-4,-6,0], [2,6,-4,0,2,-4], [-2,-5,3,1,0,3], [-2,-2,0,4,6,0]]
matriz = [[3,-3,2,0,13], [2,1,0,2,-2], [-2,2,-2,-3,-7], [2,3,-3,-2,-8]]
m = len(matriz)
c = len(matriz[0])
j = 0
while j < m:
    pivo = matriz[j][j]
    i = j+1
    while i < m:
        #print(f'i : {i}')
        fator = matriz[i][j]/ pivo
        print(fator)
        for q in range(c):
            matriz[i][q] = matriz[i][q] - fator * matriz[j][q]
        i+=1
    print("------")
    pmat(matriz, m, c)
    print("------")
    j+=1
print("matriz final:")
pmat(matriz, m, c)