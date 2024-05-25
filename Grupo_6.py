def voltear_mat(m):
    rotada=[]
    for i in range(len(m[0])):
        rotada.append([])
        for j in range(len(m)):
            rotada[i].append(m[len(m)-1-j][i])
    return rotada

#rota una matriz 90 grados en sentido del reloj

def pieza_espejo(pieza):
    piezaespejo=[]
    for fila in pieza:
        piezaespejo.append(fila[::-1])
    return piezaespejo

#invierte una matriz
#esta funcion sera utilizada adicionalmente para validar si la matriz es simetrica
#y con eso evaluar si se le sacan rotaciones o no

def nula(l,a):
    mn=[['.' for j in range(a)]for i in range(l)]
    return mn

#hace una matriz nula de L * A (largo por ancho)

def byecolum(m,n):
    colum=len(m)
    thecolum=[fila[n] for fila in m]
    borrar=['.' for i in range(colum)]
    if thecolum == borrar:
        for fila in m:
	        fila.pop(n)
    return m

def chaorow(m,n):
    row=len(m[0])
    larow=m[n]
    borrar=['.' for i in range(row)]
    if larow == borrar:
        m.pop(n)
    return m

def byebyelines(m):
    n=0
    l=len(m)
    for i in range(len(m)):
        m=chaorow(m,n)
        l2=len(m)
        if l!=l2:
            n-=1
        l=len(m)
        n+=1
    a=len(m[0])
    x=0
    for j in range(len(m[0])):
        m=byecolum(m,x)
        a2=len(m[0])
        if a!=a2:
            x-=1
        a=len(m[0])
        x+=1
    return m

#matar las lineas de la matriz que sean == [".",".",".","."]

def newpieces(l1,l2):
    piecitas=[]
    for i in range(4):
        piecitas.append(l1[i])
        piecitas.append(l2[i])
    return piecitas

def rotatepieces(P,pieces):
    rotatedpieces=[]
    flippieces=[]
    allrotatedpieces=[]
    for i in range (P):
        rotatedpieces.append(pieces[i])
        flippieces.append(pieza_espejo(pieces[i]))
        for j in range(3):
            rotatedpieces.append(voltear_mat(rotatedpieces[j]))
            flippieces.append(pieza_espejo(rotatedpieces[j+1]))
        allrotatedpieces.append(newpieces(rotatedpieces,flippieces))
        rotatedpieces=[]
        flippieces=[]
    return allrotatedpieces

#rotar todas las piezas e separarlas con index, lo mismo con los espejos, hace espejos de la pieza original y las siguientes
#rotaciones, una vez finalizado eso mediante una funcion extra se juntan las dos listas

def is_valid(tablero, pieza, fila, columna):
    filas_tablero = len(tablero)
    columnas_tablero = len(tablero[0])
    filas_pieza = len(pieza)
    columnas_pieza = len(pieza[0])
    for i in range(filas_pieza):
        for j in range(columnas_pieza):
            if fila + filas_pieza > filas_tablero or columna + columnas_pieza > columnas_tablero:
                return False
            if pieza[i][j] != '.':
                if tablero[fila + i][columna + j] != '.':
                    return False
    return True

def colocar_pieza(tablero, pieza, fila, columna):
    filas_pieza = len(pieza)
    columnas_pieza = len(pieza[0])
    for i in range(filas_pieza):
        for j in range(columnas_pieza):
            if pieza[i][j] != '.':
                tablero[fila + i][columna + j] = pieza[i][j]
    return tablero

def es_sol(t):
    t1=len(t)
    t2=len(t[0])
    for i in range(t1):
        for j in range(t2):
            if t[i][j]=='.':
                return False
    return True

def copymat(m):
    mat=nula(len(m),len(m[0]))
    for i in range(len(m)):
        for j in range(len(m[0])):
            mat[i][j]=m[i][j]
    return mat

def backtracking(piezas,tab):
    hijos=[]
    if piezas == []:
        return tab         
    if es_sol(tab):
        return tab
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            for pieza in piezas:
                if is_valid(tab,pieza,x,y):
                    t=copymat(tab)
                    t2=colocar_pieza(t,pieza,x,y)
                    hijos.append(t2)
                    break
    return hijos


def gettablero(lis):
    listilla=[]
    ir=len(lis)
    jr=len(lis[0]) 
    for i in range(ir):
        for j in range(jr):
            kr=len(lis[i][j][0])
            for k in range(kr):
                listilla.append(lis[i][j][k])
                if es_sol(lis[i][j][k]):
                    return lis[i][j][k]
    return listilla

def solution(tablero,piezas):
    pila=[]
    lista=[]
    pila.append(tablero) #tablero nulo (vacio)
    print(len(piezas))
    for j in range(len(piezas)): #len(piezas)
        lista.append(MIERDA(piezas[j],pila.pop(0)))
        print(lista)
        pila=(gettablero(lista))
    return solution(piezas,pila.pop(0))


def MIERDA(piezas,tab):
    posiciones=[]
    for pieza in piezas:
        var=(backtracking(pieza,tab))
        posiciones.append(var)
    return posiciones


def func():
    L,A,P=(input().split())
    L=int(L)
    A=int(A)
    P=int(P)
    print(L,A,P)
    pieces=[]
    piece=[]
    allpieces=[]
    line=[]
    emptytablero=nula(L,A)
    for i in range(1,(P*4)+1):
        string = input()
        if len(string)>4 or len(string)<3:
            return False
        line = [x for x in string]
        piece.append(line)
        if i%4==0:
            pieces.append(piece)
            piece=[]
    for j in range(len(pieces)):
        allpieces.append(byebyelines(pieces[j]))
    print(allpieces)
    rotatedpieces=rotatepieces(P,allpieces)
    print(rotatedpieces)
    print(len(rotatedpieces))
    for k in range(len(allpieces)):
        return(solution(nula(5,9),allpieces[k]))

#Funcion principal en la que entra el input, hace el tablero una matris de L x A (Largo x Ancho) nula, 
#y las piezas del input las pone en una lista de matrices dividida en index

print(func())