#!/usr/bin/env python
# coding: utf-8

# # MODULO SOPORTE TECNICO

# In[6]:


# Crear un diccionario de usuarios y contraseñas (esto se puede hacer en una base de datos o archivo también)
usuarios = {
    "Administrador": "contraseña1",
    "Cliente": "contraseña2",
    "Provedor": "contraseña3"
}

# Pedir al usuario que ingrese su nombre de usuario y contraseña
usuario = input("Por favor ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")

# Verificar si el usuario y la contraseña son correctos
if usuario in usuarios and usuarios[usuario] == contraseña:
    print("Bienvenido,", usuario)
else:
    print("Nombre de usuario o contraseña incorrectos")


# In[7]:


opciones = ["Cambio de clave correo", "Solicitudes VPN", "Cambio de periferico", "Instalacion de programas y/o aplicativos"]

print("Seleccione una opción:")
for i in range(len(opciones)):
    print(f"{i+1}. {opciones[i]}")

opcion_seleccionada = None
while opcion_seleccionada is None:
    try:
        seleccion = int(input("Ingrese el número de la opción seleccionada: "))
        if seleccion < 1 or seleccion > len(opciones):
            raise ValueError
        opcion_seleccionada = opciones[seleccion-1]
    except ValueError:
        print("Error: Seleccione una opción válida.")

print(f"Ha seleccionado: {opcion_seleccionada}")


# # Modulo clientes

# In[3]:


if usuario in usuarios and usuarios[usuario] == contraseña:
    solicitud = input("Seleccione el caso a solucionar: ")
    solicitud2 = input("En caso de no estar en la lista indique: otro ")
    if solicitud2 == 'otro':
        print('Indique el tipo de caso a crear')
        
    elif solicitud2 == 'No':
        # Aquí podrías poner alguna acción si el usuario responde 'No'
        print("No se seleccionó ningún caso")
    else:
        # Aquí podrías poner alguna acción si el usuario selecciona un caso de la lista
        print("Se seleccionó el caso", solicitud2)
else:
    print("Nombre de usuario o contraseña incorrectos")


# In[ ]:


if solicitud2 == 'otro'
    print('Indique cual es su solicitud')
    #Almacena las respuestas otro
    df = df['otro']
if solicitud2 == 1
    correo = input("Ingrese su correo corporativo: ")
    Nombre = input('Ingrese su nombre completo')
    cedula = input('Ingrese su numero de documento')
    
    #Almacena las respuestas otro
    df = df['otro']    


# In[ ]:




