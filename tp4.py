
S = 0
OS = 0
AP = 0
T=0
TOTAL=0
EMPLEADOS = []
X = int(input("Ingrese\n 1.COMENZAR\n 2.CERRAR"))
while X == 1:
    N = input("Ingrese nombre completo del empleado: ")
    S = float(input("Ingrese sueldo del empleado: "))
    OS = S*3/100
    AP = S*11/100
    SUELDO = (S-OS-AP)
    E = int(input("Ingrese:\n 1.SOLTERO\n 2.CASADO CON HIJOS\n 3.CASADO SIN HIJOS"))
    if E == 1:
        print ("Total a depositar a", N, "es de: $ ", SUELDO)
        TOTAL=SUELDO
    if E == 2:
        TOTAL = SUELDO + 900
        print ("El total a depositar a", N, "es de: $ ", TOTAL)
    if E == 3:
        TOTAL = SUELDO + 500
        print ("El total a depositar a", N, "es de: $ ", TOTAL)
    T=T+TOTAL
    EMPLEADOS.append(N)
    X = int(input("Ingrese\n 1.CONTINUAR\n 2.CERRAR"))
print("Empleados: ", EMPLEADOS)
print("Egresos por sueldos:$ ", T)
