SUELDO = 0
OBRASOCIAL = 0
APORTE = 0
TOTALFINAL=0
TOTAL=0
EMPLEADOS = []
IMPUESTO A LA GANANCIA
X = int(input("Ingrese\n 1.COMENZAR\n 2.CERRAR"))
while X == 1:
    NOMBRE = input("Ingrese nombre completo del empleado: ")
    SUELDO = float(input("Ingrese sueldo del empleado: "))
    OBRASOCIAL = SUELDO*3/100
    APORTE = SUELDO*11/100
    SUELDOFINAL = (SUELDO-OBRASOCIAL-APORTE)
    print("SUELDO:", SUELDO, " \n DESCUENTOS: -", OBRASOCIAL, "-", APORTE, "\n TOTAL:", SUELDOFINAL)
    ESTADO = int(input("Ingrese:\n 1.SOLTERO\n 2.CASADO CON HIJOS\n 3.CASADO SIN HIJOS"))
    if ESTADO == 1:
        print ("Total a depositar a", NOMBRE, "es de: $ ", SUELDOFINAL)
        TOTAL=SUELDOFINAL
    if ESTADO == 2:
        TOTAL = SUELDO + 900
        print ("El total a depositar a", NOMBRE, "es de: $ ", TOTAL)
    if ESTADO == 3:
        TOTAL = SUELDO + 500
        print ("El total a depositar a", NOMBRE, "es de: $ ", TOTAL)
    TOTALFINAL=TOTALFINAL+TOTAL
    EMPLEADOS.append(NOMBRE)
    X = int(input("Ingrese\n 1.CONTINUAR\n 2.CERRAR"))
print("Empleados: ", EMPLEADOS)
print("Egresos por sueldos:$ ", TOTALFINAL)
