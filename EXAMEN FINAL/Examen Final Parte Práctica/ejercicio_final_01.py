class Empleado():
    def __init__(self,nombre=0, edad=0, sueldo=0.0):
        self.nombre=nombre
        self.edad=edad
        self.sueldo=sueldo
        self.nacionalidad="peruanao"

    def solicitar_nombre(self):
        input("Ingrese el nombre del empleado: ")
    def solicitar_edad(self):
        input("Ingrese la edad del empleado: ")
    def cumpleaños(self):
        self.edad=self.edad+1
    def aumentar_sueldo(self):
        x=self.sueldo=self.sueldo+0.3*self.sueldo
        print("EL nuevo sueldo es: ".format(x))

Empleado1=Empleado("Juan",25,1000)
Empleado1.solicitar_nombre()
Empleado1.aumentar_sueldo()