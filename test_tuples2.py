from cmath import sqrt

def myRoots(p):
    a=(-p[1]+sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    b=(-p[1]-sqrt(p[1]**2-4*p[0]*p[2]))/(2*p[0])
    
    return a,b

p=[]

p.append(float(input('Ingrese coeficiente a: ')))
p.append(float(input('Ingrese coeficiente b: ')))
p.append(float(input('Ingrese coeficiente c: ')))
print(myRoots(p))