"""
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio
"""



def procesar_notas(estudiantes):
    for i in estudiantes.keys():
        prom = int((sum(estudiantes[i]) / (len(estudiantes[i]))))
        if prom>=11:
            estado="Aprobado"
        else:
            estado="Desaprobado"
        estudiantes_2={i:[prom,estado]}
        # y=estudiantes_2[i]
        # y2=y[0]
        # lista=[]
        # lista.append(y2)
        # print(lista)
        print(estudiantes_2)

estudiantes={"Luis":[18,18,15],"Pedro":[12,19,14],"Juan":[13,9,8]}

procesar_notas(estudiantes)