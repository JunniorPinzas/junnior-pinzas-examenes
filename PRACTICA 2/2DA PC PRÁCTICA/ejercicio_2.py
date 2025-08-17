"""
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""

def normalizar_nombres(nombres):
    for i in nombres:
        nombres=i.rstrip(" ")
        nombres=i.lstrip(" ")
        nombres=i.title()
        set(nombres)
        print(nombres)

nombres=["luis","victoria   ","onil pinzas","luis","   sonia","dominic","luciano    ","lionel dylan","   onil"]

normalizar_nombres(nombres)