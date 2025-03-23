import json, random, os, time
from datetime import datetime

# Variables constantes del encabezado 
AUTOR = "Cristopher robledo martinez"   # RELLENAR EN CADA PROYECTO POR FAVOR
FECHA = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
TITULO_PROYECTO = "Cajero Automático"

historial = {}      # Historial de transacciones
cantidad_dinero = random.randint(1000, 9999)    # Cantidad de dinero en el cajero

k = 0           # Generación de tickets

def ticket(t, m, f):
    global k
    k += 1
    codigo_consulta = random.randint(100, 999)
    for p in range(k):
        p += 1
        if t > 0:
            with open(f"{str(p)}ticket.txt", "w") as ticket:
                ticket.write(f"""
    ================================================================
                DEPOSITO: {m}
                Fecha: {f}
                Codigo de consulta: {codigo_consulta}                      
    ================================================================
                        """)
        elif t < 0:
            with open(f"{str(p)}ticket.txt", "w") as ticket:
                ticket.write(f"""
================================================================
            RETIRO: {m}
            Fecha: {f}
            Codigo de consulta: {codigo_consulta}                      
================================================================            
                     """)

def ver_historial():        
    limpia_pantalla()
    i = 0       # Contador para enumerar las transacciones
    for fechas, dinero in historial.items():    # Recorrer el historial de empaquetado de variables
        i += 1  
        print(f"{i} - Fecha: {fechas} - Dinero: {dinero}")  # Imprimir el historial de transacciones
    print(f"\nCantidad de dinero: {cantidad_dinero}")
    
    input("Presione enter para continuar")
    limpia_pantalla()
    interfaz()

def nip():
    # Crea el documento json si no existe
    if not os.path.exists('nip.json'):
        nip = 1010          # NIP por defecto
        # Crear el documento json
        with open('nip.json', "w") as f:
            json.dump(nip, f, indent=4)
            
    # Leer el documento json
    with open('nip.json', "r") as f:
        data = json.load(f)
    return data     # Retornar el NIP correcto

def limpia_pantalla():
    os.system("cls")       # Limpiar pantalla por defecto en Windows

def deposito_dinero():
    global cantidad_dinero
    print("Para depositar ponga los numero enteros en en positivos, en caso de retirar ponga los numeros enteros en negativos")
    dinero = int(input("Cuánto dinero desea depositar o retirar? "))
    if dinero < 0 and abs(dinero) > cantidad_dinero:            # abs() convierte el número negativo en positivo
        limpia_pantalla()
        print("No tienes suficiente dinero en el cajero")
        interfaz()
    else:   
        limpia_pantalla()
        cantidad_dinero = cantidad_dinero + dinero     # Sumar la cantidad de dinero en el cajero
        historial[datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = dinero 
        ticket(dinero, dinero, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        interfaz()
       # Guardar la fecha y la cantidad de dinero en el historial
  
def cambiar_nip():
    while True:
        nip_inicial = int(input("Ingrese su NIP actual: "))
        if nip_inicial == nip_Correcto:     # Verificar si el NIP ingresado es correcto
            nuevo_nip = int(input("Ingrese su nuevo NIP: "))
            with open('nip.json', "w") as f:        # Reinscribe el nuevo NIP en el documento json
                json.dump(nuevo_nip, f, indent=4)
            print("NIP cambiado correctamente")
            time.sleep(3)
            limpia_pantalla
            interfaz()
            break
        else:
            limpia_pantalla()
            print("el nip inicial no es correcto ")

def interfaz_inicial():
    global nip_Correcto
    nip_Correcto = nip()
    intentos = 6            # Intentos para ingresar al cajero
    while True:
        print(f"""
        ===== CAJERO AUTOMÁTICO ===== 
        Tiene {intentos} intentos para entrar al cajero
        [1] Ingresar NIP
        [2] Salir
            """)
        op = int(input("?> "))
        
        if op == 1:
            input_nip = int(input("Ingrese su NIP: "))
            if input_nip == nip_Correcto:
                limpia_pantalla()
                print("NIP correcto, Bievenido")
                interfaz()
                break
            else:
                limpia_pantalla()
                print("NIP incorrecto")
                intentos -= 1                                   
        else:
            limpia_pantalla()
            print("Gracias por usar")
            exit()
        if intentos == 0:
            limpia_pantalla()
            print("INTENTOS AGOTADOS")
            exit()
        
def interfaz():
    try:
        print("""
        ===== CAJERO AUTOMÁTICO =====
        [1] Depositar dinero o Retirar dinero
        [2] Cambiar NIP    
        [3] Ver historial de trasacciones
        [4] Salir
            """)

        op = int(input("?> "))
        
        if op == 1:
            deposito_dinero()
        elif op == 2:
            cambiar_nip()            
        elif op == 3:
            ver_historial()
        elif op == 4:
            print("Gracias por usar el cajero automático")
            exit()

    except ValueError:    # Capturar error de valor
        print("Por favor, ingrese un número entero")
        
def encabezado(f, n, t):
    print(f" \nENCABEZADO del proyecto {t}: ")
    print(f"el programa ha sido creado por {n} en la fecha {f}")
    
limpia_pantalla()        
encabezado(FECHA, AUTOR, TITULO_PROYECTO)
interfaz_inicial()