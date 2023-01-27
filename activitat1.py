from math import pi
print ( 'ACTIVIDAD 1' )
import sys
print ('Sa versio que utilizam es ' , sys.version)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 2' )

print (
'Twinkle, twinkle, little star,\n' 
'\t How I wonder what you are!\n'
'\t \t Up above the world so high,\n'  
'\t \t Like a diamond in the sky.\n' 
'Twinkle, twinkle, little star,\n'
'\t How I wonder what you are')

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 3' )

nom = input('Inserta el teu nom')
print ('El teu nom es' ,nom )

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 4' )

n = input('Inserta la teva edat')
print ('La teva edat es' ,int(n) )

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 5' )

r = int(input('Inserta el radi'))
A = pi * r ** 2
print ('L area es' ,float(A))

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 6' )

lname = input('Escriu els teus llinatges')
fname = input('Escriu el teu nom')
print(fname + ' ' + lname)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 7' )

n1 = int(input('Inserta la Primera nota'))
n2 = int(input('Inserta la Segona nota'))
n3 = int(input('Inserta la Tercera nota'))
n4 = int(input('Inserta la Cuarta nota'))
st = n1 + n2 + n3 + n4
mitja = st / 4
print ('La media de las notas es' ,float(mitja))

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 8' )

a = input('Introduce texto')
print(len(a))

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 9' )

n1 = int(input('Inserta la nota del primer examen'))
n2 = int(input('Inserta la nota del segon examen'))
nl = int(input('Inserta la nota de laboratori'))
Nf = ((60 - ( 0.3 * 65 ))/0.7) * 3 - n1 - n2
print ('La nota final que necesitas es' ,round(Nf) )

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 10' )

altura = float(input('Inserta tu altura'))
peso = float(input('Inserta tu peso en kg'))
imc = peso / altura **2
print (imc)
if imc < 16.00:
    print('Infrapeso: Delgadez Severa')
elif imc >= 16.00 and imc < 17.00:
    print('Infrapeso: Delgadez moderada')
elif imc > 17.00 and imc < 18.50:
    print('Infrapeso: Delgadez aceptable')
elif imc > 18.50 and imc < 25.00:
    print('Peso Normal')
elif imc > 25.00 and imc < 30.00:
    print('Sobrepeso')
elif imc > 30.00 and imc < 35.00:
    print('Obeso: Tipo I')
elif imc > 35.00 and imc < 40.00:
    print('Obeso: Tipo II')
elif imc > 40.00:
    print('Obeso: Tipo III')

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 11' )

sb = float(input('Inserta tu sueldo bruto'))
if sb < 1000:
    sn = sb
    print('Tu sueldo bruto es', sb ,'€' ,'Tu sueldo neto es',sn,'€')
elif sb <= 1000 and sb < 2000:
    t = sb * 0.05
    sn = sb - t
    print('Tu sueldo bruto es', sb ,'€' ,'Tu sueldo neto es',sn,'€')
elif sb <= 2000 and sb < 4000:
    t = sb * 0.10
    sn = sb - t
    print('Tu sueldo bruto es', sb ,'€' ,'Tu sueldo neto es',sn,'€')
elif sb >= 4000:
    t = sb * 0.12
    sn = sb - t
    print('Tu sueldo bruto es', sb ,'€' ,'Tu sueldo neto es',sn,'€')

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 12' )

num = float(input('Inserta un numero'))
if num < 10:
    print(num , 'Es menor que diez')
elif num > 10:
    print(num , 'Es mayor que diez')
else:
    print(num ,  'Es diez')

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 13' )

n = float(input('Inserta un numero'))
d = n % 2
if d == 0:
    print('El numero ',n,' par')
else:
    print('El numero ',n,' impar')


print ( 'ACTIVIDAD 14' )
i = 1
while(i<=10):
    print(i)
    i += 1

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 15' )

e = float(input('En que año estamos'))
c = float(input('Escribe un año cualquiera'))
if e < c:
    x = e - c
    print('Para llegar al año', c , 'fltan', x ,'años')
elif e > c:
    x = e - c
    print('Han pasado ', x , 'años desde', c ,'años')
else :
    print('Son el mismo año')

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 16' )

dividendo = float(input('Escribe el dividendo'))
divisor = float(input('Escribe el divisor'))
division = dividendo / divisor
n = dividendo % divisor
if n == 0:
    print('Cociente:',division,)
else :
    print('Cociente:',division, 'Resto',n,)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 17' )

e = float(input('Escribe un numero'))
c = float(input('Escribe otro numero'))
if e < c:
    print('Mayor:' ,c, 'Menor:' ,e,)
elif e > c:
    print('Mayor:',e, 'Menor:' ,c,)
else :
    print('Son iguales')


------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 18' )

e = float(input('Escribe un numero'))
c = float(input('Escribe otro numero'))
d = e / c
h = d % 2
if e >= c:
    d = e / c
    h = d % 2
    if h== 0:
        print(e,'es multiple de',c)
    else:
        print(e,'es multiple de',c)
else:
    d = c / e
    h = d % 2
    if h== 0:
        print(c,'es multiple de',e)
    else:
        print(c,'es multiple de',e)


------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 19' )

e = float(input('Escribe un numero'))
c = float(input('Escribe otro numero'))
a = float(input('Escribe otro numero'))
if e==c and e==a:
    print('Los tres numeros son iguales')
elif c==a or a==e or c==e:
    print('Dos numeros son iguales')
else:
    print('Ningun numero es igual')


------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 20' )

a = float(input('Escribe un año y te dire si es bisiesto'))
b = a % 4
c = a % 400
d = a % 100
if b==0 and c==0 or d !=0:
    print('El año',round(a),'es bisiesto')
else:
    print('El año',round(a),'no es bisiesto')


------------------------------------------------------------------------------------------------------------------------
from math import pi
print ( 'ACTIVIDAD 21' )

y = input('Que quieres calcular el area del triangulo=t o del circulo=c')
if y == 't' :
    b = float(input('Escribe la base'))
    a = float(input('Escribe la altura'))
    o = b * a / 2
    print('El area del triangulo es',float(o))
elif y == 'c' :
    r = float(input('Escribe el radio'))
    w = pi * r**2
    print('El area del circulo es',float(w))
else :
    print('ERROR')


------------------------------------------------------------------------------------------------------------------------
from math import trunc
print ( 'ACTIVIDAD 22' )

cm = float(input('Escribe una distancia en centimetros'))
if cm < 100 :
    print('Tu distancia es',cm,'cm')
elif cm >= 100 and cm < 1000 :
    m = cm / 100
    cm2 = m - trunc(m)
    m2 = m - cm2
    print('Tu distancia es',round(m2),'m y',round(cm2),'cm')
elif cm >= 1000 and cm < 1000000 :
    km = cm / 1000000
    x = km - trunc(km)
    km1 = km - x
    m3 = km * 100
    cm3 = m3 - trunc(m3)
    m4 = m3 - cm3
    print('Tu distancia es',round(km1),'km,',round(m4),'m y',round(cm3),'cm')


------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 23' )

a = int(input('Escribe un numero'))
if a == 0 :
    print('Los numeros que has escrito son',a)
else :
    b = [a]
    while True:
        c = int(input('Escribe otro numero'))
        if c == 0 :
            print('Los numeros que has escrito son',b)
            break
        else :
            b.append(c)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 24' )

a = float(input('Escribe una nota'))
if a < 0 or a > 10 :
    print('Las notas que has escrito son',a)
else :
    b = [a]
    while True:
        c = float(input('Escribe otra nota'))
        if c < 0 or c > 10 :
            print('Las notas que has escrito son',b)
            break
        else :
            b.append(c)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 25' )

a = int(input('Escribe un numero'))
h = int(input(print('Escribe un numero mayor que ',a )))
if a > h :
    print('Los numeros que has escrito son',a ,h)
else :
    b = [a,h]
    while True:
        c = int(input('Escribe otro numero'))
        if c > h :
            print('Los numeros que has escrito son',b)
            break
        else :
            b.append(c)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 26' )

a = int(input("Escribe un numero "))
h = int(input(f"Escribe un numero mayor que {a} "))
if a > h:
    print("Los numeros que has escrito son", a, h)
else:
    b = []
    while True:
        c = int(input("Escribe otro numero"))
        if c > h or c < a:
            print(f"Los numeros entre {a} y {h} que has escrito son: {b}")
            break
        else:
            b.append(c)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 27' )

x = int(input("Escribe un numero limite "))
c = 0
b = []
y = 0
while True:
    if c >= x:
        print("El limite es ",x," , que has escrito son: ",b )
        break
    else:
        y = int(input("Escribe un numero"))
        b.append(y)
        c = c+y

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 28' )
import random
y = int(input("Escribe un numero minimo"))
z = int(input("Escribe un numero maximo"))
x = random.randrange(y,z)
print(f"A ver si adivinas un numero entre {y} y {z}")
a = int(input("Escribe un numero"))
b = 0
while True:
    if a < x:
        b = b + 1
        a = int(input("¡Demasiado pequeño! Intentalo de nuevo" ))
    elif a > x:
        b = b + 1
        a = int(input("¡Demasiado grande! Intentalo de nuevo" ))
    elif a == x:
        print(f"¡Has acertado!Te ha costado {b} intentos")
        break

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 29' )

x = list(range(1000,99,-100))
print(x)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 30' )

a = int(input("Dime un numero positivo" ))
if a < 0:
    a = int(input("Dime un numero positivo" ))
y = a + 1
z = a - 1
h = -1
x = list(range(0,y,1))
print(x)
x = list(range(a,h,-1))
print(x)
x = list(range(1,a,1))
print(x)
x = list(range(z,0,-1))
print(x)
x = (list(range(0,a,1)))+(list(range(a,h,-1)))
print(x)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 31' )

a = int(input("Dime un numero" ))
if a > 0 :
    b = a + 1
    x = list(range(0,b,1))
    print(x)
else :
    h = a -1
    x = list(range(0,h,-1))
    print(x)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 32' )

while True:
    a = int(input("Dime un numero " ))
    b = int(input(f"Dime un numero mayor que {a}" ))
    if a >= b:
        print("Te he dicho mayor que ",a)
    else :
        y = a + 1
        z = a - 1
        t = b + 1
        h = b - 1
        u = b + 2
        x = list(range(a,t,1))
        print(x)
        x = list(range(h,z,-1))
        print(x)
        x = list(range(y,u,1))
        print(x)
        x = list(range(h,a,-1))
        print(x)
        x = (list(range(a,b,1)))+(list(range(b,z,-1)))
        print(x)
        break

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 33' )

a = int(input("Dime un numero" ))
b = int(input("Dime otro numero" ))
if a < b :
    p = b + 1
    x = list(range(a,p,1))
    print(x)
else :
    h = b - 1
    x = list(range(a,h,-1))
    print(x)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 34' )

while True:
    a = int(input("Dime un numero " ))
    b = int(input("Dime otro numero" ))
    if a > b :
        b = b + 1
        x = (list(range(b,a,1)))
        print(x)
        break
    elif b > a :
        a = a + 1
        x = (list(range(a,b,1)))
        print(x)
        break

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 35' )

a = int(input("Dime un numero " ))
b = int(input("Dime cuantos numeros quieres" ))
h = a + b
x = (list(range(a,h,1)))
print(x)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 36' )

while True:
    a = int(input("Dime un valor inicial " ))
    b = int(input("Dime un valor final" ))
    h = a % 2
        if h == 1:
            a = a + 1
            b = b + 1
            x = (list(range(a,b,2)))
            print(x)
            break
        elif h == 0 :
            b = b + 1
            x = (list(range(a,b,2)))
            print(x)
            break
        else :
            print("Error")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 37' )

while True:
    a = int(input("Dime un valor inicial " ))
    b = int(input("Dime un valor final" ))
    c = int(input("De que numero quieres los multiples?" ))
    h = a % c
        if h == 1:
            a = a + 1
            b = b + 1
            x = (list(range(a,b,5)))
            print(x)
            print(f"Entre{a} i {b} hi ha  ")
            break
        elif h == 0 :
            b = b + 1
            x = (list(range(a,b,5)))
            print(x)
            break
        else :
            print("Error")



------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 38' )

a = int(input("Dime un numero " ))
b = int(input("Dime otro numero" ))
c = 0
j = []
for i in range(a,(b+1),1):
    c = c + i
    j.append(i)
print(j)
print(f"La suma desde {a} hasta {b} es: {c} ")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 39' )

a = int(input("Dime cuantos numeros vas a escribir " ))
c = 0
for i in range(a):
    b = int(input(f"Dime el numero {i + 1}" ))
    c = c + b
print(f"La suma de los numeros que has escrito es {c} ")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 40' )

a = int(input("Dime cuantos numeros vas a escribir " ))
c = 0
for i in range(a):
    b = int(input(f"Dime el numero {i + 1}" ))
    if b < 0:
        c = c + 1
    else :
        c = c + 0

print(f"Has escrit {c} numeros negativos ")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 41' )

a = int(input("Dime cuantos numeros vas a escribir " ))
c = 0
t = []
for i in range(a):
    b = int(input(f"Dime el numero {i + 1}" ))
    c = c + b
    t.append(b)
r = min(t)
u = max(t)
h = c / a
print(f"El número más pequeño de los introducidos es:{r} ")
print(f"El número más grande de los introducidos es:{u} ")
print(f"La media de los números introducidos es:{h} ")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 42' )

a = int(input("Anchura del rectángulo:" ))
b = int(input("Altura del rectángulo:" ))
for i in range(b):
    print("*"*a)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 43' )

b = int(input("Altura del triangulo:" ))
for i in range(b+1):
    print("*"*i)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 44' )

b = int(input("Altura del triangulo:" ))
for i in range(b,0,-1):
    print("*"*i)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 45' )

b = int(input("Altura del triangulo:" ))
for i in range(b):
    print("*"*i)
for i in range(b,0,-1):
    print("*"*i)

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 46' )

b = int(input("Altura del triangulo:" ))
for i in range(b+1):
    print("*"*i)
No esta hecha


------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 54' )
x = input("Usuario")
if len(x) < 6:
    print("El nombre de usuario debe contener al menos 6 caracteres")
elif len(x) > 12:
    print("El nombre de usuario no puede contener más de 12 caracteres")
elif x.isalnum()== False:
    print("El nombre de usuario puede contener solo letras y números")
else:
    print("Usuario correcto")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 55' )

x = input("Contraseña")
if len(x) < 8 :
    print("La contraseña debe contener al menos 8 caracteres")
elif x.isalnum()== True:
    print("La contraseña debe contener al menos un caracter no alfanumerico")
elif x.isupper()== True:
    print("La contraseña debe contener al menos un caracter en mayusculas")
elif x.islower()== True:
    print("La contraseña debe contener al menos un caracter en minuscula")
elif x.isspace()== False:
    print("La contraseña no debe contener espacios es blanco")
else:
    print("Contraseña correcta")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 56' )

x = input("Usuario")
y = input("Contraseña")
if len(x) < 6:
    print("El nombre de usuario debe contener al menos 6 caracteres")
elif len(x) > 12:
    print("El nombre de usuario no puede contener más de 12 caracteres")
elif x.isalnum()== False:
    print("El nombre de usuario puede contener solo letras y números")
elif len(y) < 8 :
    print("La contraseña debe contener al menos 8 caracteres")
elif y.isalnum()== True:
    print("La contraseña debe contener al menos un caracter no alfanumerico")
elif y.isupper()== True:
    print("La contraseña debe contener al menos un caracter en mayusculas")
elif y.islower()== True:
    print("La contraseña debe contener al menos un caracter en minuscula")
elif y.isspace()== True:
    print("La contraseña no debe contener espacios es blanco")
else:
    print("El usuario y la contraseña son correctos")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 59' )

a = int(input("Cuantos datos vas a ingresar? " ))
c = 0
r = 0
f = []
m = 0
y = 0
for a in range(1,a+1):
    c = c + 1
    b = float(input(f"Dato {c} " ))
    y = y + b
    f.append(b)
m = m + y
x = m / a
for a in f:
    if a > x:
        r = r+1
print(f"{r} datos son mayores que el promedio")

------------------------------------------------------------------------------------------------------------------------

print ( 'ACTIVIDAD 60' )

def contar_letras(x):
    d = { }
    x = x.lower()
    for i in x:
        if i.isalpha():
            if i in d:
                d[i] += 1
            elif i not in d :
                d[i] = 1
    return x

print(contar_letras)

y = input("Escribe lo que quieras")
print(contar_letras(y))




