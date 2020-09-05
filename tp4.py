
S = 0
OS = 0
AP = 0
EMPLEADOS = []
X = int(input("Ingrese\n 1.COMENZAR\n 2.CERRAR"))
while X == 1:
    N = input("Ingrese nombre completo del empleado: ")
    S = float(input("Ingrese sueldo del empleado: "))
    OS = S*3/100
    AP = S*11/100
    SUELDO = (S-OS-AP)
    E = int(input("Ingrese:\n 1.SOLTERO\n 2.CASADO CON HIJOS\n 3.CASADO SIN HIJOS"))

    
