from numpy import size
import calculus
import math
import matplotlib.pyplot as plt

def f1(x):
    return 2*x*x +3
lista_x,lista_fx = calculus.der(f1,0,1,0.01)
plt.scatter(lista_x,lista_fx,s=1)

def f1_int(x):
    return (2/3)*x**3 + 3*x

print(calculus.der_point(f1,1,0.01))
plt.show()

n_list = []
y_list = []
upper_list = []
lower_list = []
for n in range(100,5000,100):
    upper,lower = calculus.integral(f1,0,1,n)
    upper_list.append(upper)
    lower_list.append(lower)
    n_list.append(n)
    y_list.append(f1_int(1) - f1_int(0))
plt.scatter(n_list,upper_list,s=1)
plt.scatter(n_list,lower_list,s=1)
plt.plot(n_list,y_list)
plt.show()


#x_lista,listaa = calculus.trapez(f1,0,1,0.1)
#plt.plot(x_lista,listaa)
#plt.show()