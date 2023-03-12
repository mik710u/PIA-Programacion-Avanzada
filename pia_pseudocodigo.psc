Algoritmo Veterinaria
    Definir opcion, clave Como Entero
    Definir nombre, tipo, raza, peso, fecha_consul Como Cadena
    Definir encontrado Como Logico
    
    registros <- Vacio
    
    Mientras opcion <> 0 Hacer
        Escribir "-- MENU VETERINARIA --"
        Escribir "[1] Agregar mascota atendida"
        Escribir "[2] Consultar mascota atendida"
        Escribir "[3] Ver todas las mascotas atendidas"
        Escribir "[0] Salir"
        Leer opcion
        
        Segun opcion Hacer
            1:  Escribir "Ingrese los datos de la mascota:"
                Leer clave
                Leer nombre
                Leer especie
                Leer raza
                Leer peso
		Leer fecha_consul
                registros <- registros + [clave, nombre, tipo, raza, peso, fecha_consul]
                Escribir "Se ha registrado la mascota"
				
            2:  encontrado <- Falso
                Escribir "Ingrese la clave de la mascota a consultar:"
                Leer clave
                Para i <- 1 Hasta Longitud(registros) Con Paso 5 Hacer
                    Si registros[i] = id Entonces
                        Escribir "Clave:", registros[i]
                        Escribir "Nombre:", registros[i+1]
                        Escribir "Especie:", registros[i+2]
                        Escribir "Raza:", registros[i+3]
                        Escribir "Peso:", registros[i+4]
						Escribir "Fecha:", registros[i+4]
                        encontrado <- Verdadero
                    FinSi
                FinPara
                Si encontrado = Falso Entonces
                    Escribir "No se encontró la mascota con la clave ingresada"
                FinSi
				
            3:  Si Longitud(registros) = 0 Entonces
                    Escribir "No hay registros"
                Sino
                    Para i <- 1 Hasta Longitud(registros) Con Paso 5 Hacer
						Escribir "Clave:", registros[i]
                        Escribir "Nombre:", registros[i+1]
                        Escribir "Especie:", registros[i+2]
                        Escribir "Raza:", registros[i+3]
                        Escribir "Peso:", registros[i+4]
						Escribir "Fecha:", registros[i+4]
                    FinPara
                FinSi
				
            0:  Escribir "-- Fin del programa --"
				
            De Otro Modo: Escribir "Opcion invalida. Intente de nuevo"
        FinSegun
    FinMientras
	
	
FinAlgoritmo
