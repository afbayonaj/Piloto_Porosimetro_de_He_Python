#import time
#import datetime
import math

#=================================================================================
# El siguiente es el modulo de logeo...
#=================================================================================
listaUsuario=["admin"]
listaContraseña=[123456]

def validarUsario():
	eleccionIngresada=False
	nombreUsuario=False
	logeo=False
	
	while eleccionIngresada==False:
		eleccion=input("Para iniciar sesion digite 1, Para registrarse digite 2: ")
		if eleccion=="1":
			eleccionIngresada=True
			
			while nombreUsuario==False:
				usuario=input("\nDigite su Usuario: ")
				if (usuario in listaUsuario)==True:
					indiceContraseña=listaUsuario.index(usuario)
					nombreUsuario=True
					
					while logeo==False:
						contraseña=int(input("\nDigite su contraseña: "))
						if contraseña==(listaContraseña[int(indiceContraseña)]): # Pendiente excepcion para texto y numero de intentos fallidos
							logeo=True
							print("\nUsuario y contraseña correctos!! \n\nCargando pagina...")

							validarModulo=False
							modulo=input("\nSeleccion el procedimiento que desee realizar:\n\nPara volumen total digite (1):\nPara volumen de grano digite (2)\nPara permeabilidad convencional (3):\nPara finalizar (0)\n\n")
							
							while validarModulo==False:
								if modulo=="1":
									validarModulo=True
									volumenCilindro()
								elif modulo=="2":
									validarModulo=True
									volumenGrano()
								elif modulo=="3":
									validarModulo=True
									permeabilidadConv()
								else:
									print("\nOpcion no valida, seleccione una de las 3 opciones: ")
						else:
							print("\nContraseña incorrecta")
				else:
					print("\nUsuario no registrado por favor verifiquelo")
		elif eleccion=="2":
			eleccionIngresada=True
			registroUsuarioNuevo()
		else:
			print("\nOpcion no valida por favor seleccione una opcion entre 1 y 2")

#=================================================================================
# El siguiente es el modulo de registro para nuevos usuario...
#=================================================================================
def registroUsuarioNuevo():
	registroNuevo=False

	usuarioNuevo=input("\nDigite nombre de Usuario: ")
	listaUsuario.append(usuarioNuevo)
	
	while registroNuevo==False:
		contraseñaUN=input("\nDigite una contraseña numerica de minimo 6 digitos: ")
		if len(contraseñaUN)>=6 and contraseñaUN.isdigit()==True:
			registroNuevo=True
			contraseñaUN=int(contraseñaUN)
			listaContraseña.append(contraseñaUN)
		else:
			print("Contraseña incorrecta, recuerdo que debe ser numerica de minimo 6 digitos...")
	
	sexo=input("\nSeleccione su sexo; para masculino digite (M) para femenino (F): ")
	sexo=sexo.upper()

	while sexo!="M" and sexo!="F": 
		sexo=input("Opcion no valida digite (M) o (F): ")
		sexo=sexo.upper()

	edad=input("\nDigite su edad: " )

	while edad.isdigit()==False:
		edad=input("Su edad debe ser un valor numerico: ")
	
	celular=input("\nDigite el numero de celular: " )

	while celular.isdigit()==False:
		celular=input("El numero de celular debe ser un valor numerico: ")

	print("\nSu registro se ha realizado de forma exitosa!!\n")
	
	for i in range(3):
		print(".\n")

	sesion=input("\nsi desea iniciar sesion digite 1 para finalizar digite 0: ")
	print("\n")
	estadoSesion=False

	while estadoSesion==False:
		if sesion=="1":
			estadoSesion=True
			validarUsario()
		elif sesion=="0":
			estadoSesion=True
			print("\nProceso finalizado, Gracias por Visitarnos!!")
		else:
			sesion=input("Opcion no valida por favor seleccione 1 o 0: ")

#=================================================================================
# El siguiente es el modulo para calculo de volumen total de un cilindro...
#=================================================================================
def volumenCilindro():
	validarDiametro=False
	validarLongitud=False
	modulo1=True

	while modulo1==True:
		print("\nPara calcular el volumen de un cilindro digite los siguientes datos:\n")

		while validarDiametro==False:
			try:
				diametro=float(input("Diametro del cilindro(cm): "))
				validarDiametro=True
			except (TypeError, ValueError):
				print("\nEl diametro del cilindro debe ser un valor numerico en (cm)!!!")

		while validarLongitud==False:
			try:
				longitud=float(input("Longitud del cilindro(cm): "))
				validarLongitud=True
			except (TypeError, ValueError):
				print("\nLa longitud del cilindro debe ser un valor numerico en (cm)!!!")

		volCilindro=round((math.pi*(diametro/2)**2)*longitud, 3)
		print("\nEl volumen total del cilindro es: " + str(volCilindro) + " cc")
		continuar=input("\nPara calcular un nuevo volumen digite (1) para terminar digite (0): ")
		
		while continuar!="1" and continuar!="0":
			continuar=input("\nDebe seleccionar una de las dos opciones: Nuevo Volumen(1) Terminar(0): ")

		if continuar=="0":
			modulo1=False
		elif continuar=="1":
			print("\nVamos con el siguiente...\n")

#=================================================================================
# El siguiente es el modulo para calculo de volumen de grano...
#=================================================================================
def volumenGrano():
	validarPR=False
	validarPE=False
	calVolDiscos1=[43.6268438358188, 40.9114301139499, 35.4549784755074, 31.3684356953094, 25.9119840568669, 21.828163260929, 16.3521782574941, 10.8957266190516, 5.45645163844253, 1.36268152145784]
	calPrPe1=[1.24462809917355, 1.28869883934026, 1.37967564739733, 1.44818119423473, 1.53932584269663, 1.6071918330032, 1.69882428732485, 1.7906265919511, 1.88070613409415, 1.94951923076923]
	calVolDiscos2=[95.545, 2.986, 35.82, 83.59, 71.669, 53.746, 41.796, 26.892, 14.914, 65.667]
	calPrPe2=[1.28091155234657, 2.83250249252243, 2.2815826471179, 1.48044838373306, 1.68002365813988, 1.97960251046025, 2.17949702438088, 2.42835724994646, 2.62953488372093, 1.77982373308152]
	lisDiscos1=[0, 1.36268152145784, 1.35273220041108, 2.73108859552685, 5.45645163844253, 10.8957266190516, 21.828163260929]
	lisDiscos2=[0, 2.986, 2.993, 5.976, 11.921, 23.899, 47.77]
	presionAtmosferica=0
	volDiscos=0

	lp1=[]

	sumax1=0
	sumay1=0
	sumae1=0
	sumac1=0
	contadorx1=0
	contadory1=0
	z=0

	lp2=[]

	sumax2=0
	sumay2=0
	sumae2=0
	sumac2=0
	contadorx2=0
	contadory2=0
	zz=0

# Calibracion para 1 pulgada:

	for x in calPrPe1:
		sumax1=sumax1+x
		contadorx1+=1

	for y in calVolDiscos1:
		sumay1=sumay1+y
		contadory1+=1

	promediox1=sumax1/contadorx1
	promedioy1=sumay1/contadory1

	for e in calPrPe1:
		lp1.append(-((calPrPe1[z]-promediox1)*(calVolDiscos1[z]-promedioy1)))
		sumac1=sumac1+((e-promediox1)**2)
		sumae1=sumae1+lp1[z]
		z+=1

# Calibracion para 1.5 pulgadas:

	for p in calPrPe2:
		sumax2=sumax2+p
		contadorx2+=1

	for q in calVolDiscos2:
		sumay2=sumay2+q
		contadory2+=1

	promediox2=sumax2/contadorx2
	promedioy2=sumay2/contadory2

	for t in calPrPe2:
		lp2.append(-((calPrPe2[zz]-promediox2)*(calVolDiscos2[zz]-promedioy2)))
		sumac2=sumac2+((t-promediox2)**2)
		sumae2=sumae2+lp2[zz]
		zz+=1

	pendiente1=sumae1/sumac1
	intercepto1=promedioy1+(pendiente1*promediox1)

	pendiente2=sumae2/sumac2
	intercepto2=promedioy2+(pendiente2*promediox2)

	print("\nPendiente 1 pulgada: " + str(pendiente1))
	print("intercepto 1 pulgada: " + str(intercepto1))
	print("Pendiente 1.5 pulgadas: " + str(pendiente2))
	print("intercepto 1.5 pulgadas: " + str(intercepto2))

	# pendiente=sumatoria(x-prom(x))(y-prom(y))/(x-prom(x))^2 -- Minimos cuadrados

	'''
	Los valores de la calibracion son 
	pendiente, intercepto, Pref, Rango de Vol, Error
	'''

	eleccionProceso=input("\nPara medir volumen de grano digite (1), Para calibrar digite (2): ")

	while eleccionProceso!="1" and eleccionProceso!="2":
		eleccionProceso=input("\nDebe seleccionar una de las dos pociones:\nPara medir volumen de grano (1), Para calibrar digite (2): ")

	if eleccionProceso=="1":
		portamuestra=input("\nSeleccione el diametro del portamuestra:\n\nPara 1 pulgada digite (1)\nPara 1.5 pulgadas digite (2)\nPara finalizar digite (0)\n\nCual elige: ")
		
		if portamuestra=="1":
			pendiente=pendiente1
			intercepto=intercepto1
			discos=input("\nDigite los discos utilizados: ")
		
			while discos.find("0")==-1 and discos.find("1")==-1 and discos.find("2")==-1 and discos.find("3")==-1 and discos.find("4")==-1 and discos.find("5")==-1 and discos.find("6")==-1:
				discos=input("Valor no valido, deben ser valores de 1 a 6: ")

			for l in discos:
				if l=="" or l=="0":  # Forma larga de calcular volDiscos
					volDiscos=volDiscos+lisDiscos1[0]
				elif l=="1":
					volDiscos=volDiscos+lisDiscos1[1]
				elif l=="2":
					volDiscos=volDiscos+lisDiscos1[2]
				elif l=="3":
					volDiscos=volDiscos+lisDiscos1[3]
				elif l=="4":
					volDiscos=volDiscos+lisDiscos1[4]
				elif l=="5":
					volDiscos=volDiscos+lisDiscos1[5]
				elif l=="6":
					volDiscos=volDiscos+lisDiscos1[6]
			
		elif portamuestra=="2":
			pendiente=pendiente2
			intercepto=intercepto2
			discos=input("\nDigite los discos utilizados: ")
		
			while discos.find("")==-1 and discos.find("0")==-1 and discos.find("1")==-1 and discos.find("2")==-1 and discos.find("3")==-1 and discos.find("4")==-1 and discos.find("5")==-1 and discos.find("6")==-1:
				discos=input("Valor no valido, deben ser valores de 0 a 6: ")

			for c in discos: # Forma corte de calcular volDiscos
				if c.isdigit()==True:
					volDiscos=volDiscos+lisDiscos2[int(c)]

		elif portamuestra=="0":
			print("\nModulo finalizado!!!")
		else:
			print("\nSeleccione una de las tres opciones diponibles...\n")

		while validarPR==False:
			try:
				presionRefrencia=float(input("\nIngrese la presion de referencia (psi): "))
				validarPR=True
			except (TypeError, ValueError):
				print("\nLa presion de referencia debe ser numerica por favor verifiquela!!")

		while validarPE==False:
			try:
				presionExpansion=float(input("\nIngrese la presion de expansion (psi): "))
				validarPE=True
			except (TypeError, ValueError):
				print("\nLa presion de expansion debe ser numerica por favor verifiquela!!")
		
		volGrano=pendiente*(presionRefrencia/presionExpansion)+intercepto-volDiscos
		print("\nEl volumen de grano es: " + str(volGrano) + " gr/cc")

	elif eleccionProceso=="2":
		diametroCalibrar=input("Para calibracion de 1 pulgada digite (1), para 1.5 pulgadas digite (2): ")

		while diametroCalibrar!="1" and diametroCalibrar!="2":
			diametroCalibrar=input("Opcion no valida seleccione (1) para 1 pulgada o (2) para 1.5 pulgadas: ")

		if diametroCalibrar=="1":
			print("")
		elif diametroCalibrar=="2":
			print("")  
	
#=================================================================================
# El siguiente es el modulo para calculo de permeabilidad convencional
#=================================================================================
def permeabilidadConv():
	pass

validarUsario()