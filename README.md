# Cajero Automático - Practica hecha en Python 
Por: Cristopher Baltazar Robledo Mártinez

## Sistemas de archivos
/proyecto
│── main.py          # Código principal
│── nip.json	     # Archivo donde almacenará localmente el NIP sin encriptaciones o restricciones al usuario de acceder al archivo 
└── README.md        # Este archivo

## Esctrucura del código 
### Funciones:
- ver_historial(): Es la parte que se encarga de ver el historial de trasacciones
	hechas por el usuario con su fecha y monto agregado. Además en la parte 
	de abajo se almacena la cantidad total de dinero generado aleatoriamente
	entre un rango de 1000 - 9999
	
	#### Estrucutura de control:
	1. comienza generando un contador para agregar un contador de trasacciones
	2. genera un bucle en forma de empaquetado de diccionarios a variables del 
	bucle para que puedan almacenarse de forma separada por clave(fechas) y valor(dinero).
	3. Dependiendo del numero de elementos hara un bucle y cada recorrido será un agregado de datos (aunque hay que tomar en cuenta que es un historial no fijo) 
	4. Muestra el numero de elementos, con un numero de índice, fecha y la cantidad de dinero agregada o retirada 

- nip(): Es la que se encarga de almacenar en una base de datos locales de forma ligera 
	en json. Principalmente el Nip que sería como una contraseña para acceder al cajero. 
	Sin el nip no dará acceso al nip y eso se ve en la función "interfaz_inicial()"

	#### Estrucutura de control:
	1. en caso que no exista el archivos "nip.json" se crear uno con nip inicial que es 1010
	2. leé el documento json y lo retorna como "data".

- deposito_dinero(): Es una función sirve para depositar o retirar el dinero. 

	#### Estrucutura de control:
	1. Se declara la variable global "cantidad dinero" para que tanto la función "historial" pueda acceder a el sin ningun problema
	2. se le pide esctritamente en entero la cantidad de dinero a depositar o retirar
	3. verificar si dinero no es menor a la cantidad actual dinero, en caso que sea cierto no dejará retirar, solo depositara

- cambiar_nip(): el usuario podra cambiar el nip fijo sin ningun problema guardado en archivo nip.json
	
	#### Estrucutura de control:
	1. primero le pide el nip actual y compruba que sea el correcto 
	2. Si es el nip correcto le pide el nuevo nip que quiere agregar
	3. se modifica de forma permanente el nip.json 
- interfaz_inicial(): es la interfaz que inicia con el bloque de acceso para entrar
	en si al cajero 

	#### Estrucutura de control:
	1. primero tendra un numero de intentos, en caso de acabar los 6 intentos se terminara cerrando el programa en automático
	2. tendra dos opciones para entrar o para salir
	3. para entrar debera de poner el nip inicial o el modificado para entrar a la interfaz del cajero 

- interfaz(): El intefaz se encarga de pedirle al usuario las opciones para ejecutar las funciones anteriormente 
	mencionadas como ver_historial, nip, deposito_dinero, cambiar, nip.

Notas de desarrollador:
* Primero hay que entender que los valores como el historial de trasacciones no se guarda ni la cantidad. Cada vez que se inicia un el programa vuelve a generarse
un valor de monetario de forma aleatoria. No es fija como el nip que se almacena en un "nip.json"
* En caso que se quiera iniciar de nuevo con la nip por defecto, se puede eliminar el archivo "nip.json" y en automático el programa detectará al ausencia de este 
y creeará uno nuevo por defecto con una contraseña fija para archivos "nip.json" recien hechos. También es muy importante respestar el nombre del archivo para sea detectado en automático por el programa









