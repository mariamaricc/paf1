def der_point(f,x,h):
    return((f(x+h)-f(x))/h)



def der(f,a,b,h):
    lista = []
    lista_x = []
    n = int((b-a)/h)
    for i in range (n):
        lista.append(der_point(f,a+i*h,h))
        lista_x.append(a+i*h)
    return(lista_x,lista)
    

def integral(f,a,b,n):
    upper = 0
    lower = 0
    h = (b-a)/n
    x = a
    while x < b:
        f_u = h*f(x)
        f_l = h*f(x-h)
        upper += f_u
        lower += f_l
        x += h

    return(upper,lower)

def trapez(f,a,b,h):
    listaa = []
    x_lista = []
    n = int((b-a)/h)
    for i in range (1,n+1):
        f_x = h/2*((f(a)-f(b))/2)
        listaa.append(f_x)
        x_lista.append(i*h)
    return(x_lista,listaa) 