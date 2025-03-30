#Diccionario La sección "Acceder y Modificar Valores" menciona agregar "profesion", pero esta clave ya está en la creación del diccionario. Podrías reformularlo como "Modificar la profesión existente o agregar otra clave relacionada


infopers_diccionario ={
 "nombre":"Lady",
 "edad":"17",
 "ciudad":"Sucumbios",
 "Profección":"en_transcurso"
  }

# modificar la ciudad
infopers_diccionario["ciudad"] = "Nueva loja"

# verificar si calve del "telefono" existe , si no agregar
if "telefono" not in infopers_diccionario:
    infopers_diccionario["telefono"] = "0989726029"

# eliminar la clave "edad"
del infopers_diccionario ["edad"]

#imprimir el diccionaro 
print (infopers_diccionario)

