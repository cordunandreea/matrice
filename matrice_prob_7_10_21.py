n=int(input('Introduceti de la tastatura numarul n de linii:'))
c=[]
e=[]
g=[]
k=[]
l=[]
m=[]
if n>=2 and n<=10:
    matrice=[]
    print('introduceti valorile pe ordine orizontala:')
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input()))
        matrice.append(x)
    for i in range(n):
        for j in range(n):
            print(matrice[i][j], end=' ')
        print()
for i in range(n):
    for j in range(n):
        if i==j:
            c.append(matrice[i][j])
z=sum(c)
print('suma componentelopr de pe diagonala principala:',z)
for i in range(n):
    for j in range(n):
        if ((i+j) == (n-1)):
            e.append(matrice[i][j])
q=sum(e)
print('suma componentelopr de pe diagonala secundara:',q)
for i in range(n):
    for j in range(n):
        if i>j:
            g.append(matrice[i][j])
a=sum(g)
print('suma componentelopr mai jos de diagonala principala:',a)
for i in range(n):
    for j in range(n):
        if i<j:
            k.append(matrice[i][j])
f=sum(k)
print('suma componentelopr mai sus de diagonala principala:',f)
for i in range(n):
    for j in range(n):
        if ((i+j) < (n-1)):
            l.append(matrice[i][j])
p=sum(l)
print('suma componentelopr mai sus de diagonala secundara:',p)
for i in range(n):
    for j in range(n):
        if ((i+j) > (n-1)):
            m.append(matrice[i][j])
s=sum(m)
print('suma componentelopr mai jos de diagonala secundara:',s)