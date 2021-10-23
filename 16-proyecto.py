import os

CARPETA = 'contactos/'
EXTENSION ='.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
          
        

def app():
    
     
    crear_directorio()
    
    
    mostrar_menu()
    
    preguntar=True
    while preguntar:
        opcion = input('\r\n Seleccione una opcion:\r\n')
        opcion = int(opcion)
        
        #ejecutar las opciones
        if opcion==1:
            agregar_contacto()
            
            preguntar=False
        elif opcion==2:
            editar_contacto()
            preguntar=False
        elif opcion==3:
            ver_contactos()
            preguntar=False
        elif opcion==4:
            buscar_contacto()
            preguntar=False
        elif opcion==5:
            eliminar_contacto()
            preguntar=False
        else:
            print("Opcion no valida")
            app()    
def eliminar_contacto():
    try:
        nombre = input('\r\nEscriba contacto a eliminar:\r\n')
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nContacto Eliminado\r\n')
    except (IOError):
        print('No existe ese contacto!!!')
    app()
def buscar_contacto():
    try:
        nombre = input('\r\nEscribe el contacto que deseas buscar:\r\n')
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\nInformacion del contacto:\r\n')
            for linea in contacto:
                print (linea.rstrip())
            print('\r\n')
    except IOError:
        print('El Archivo no existe con nombre '+ nombre)
        print(IOError)
    app()
                
def ver_contactos():
    archivos = os.listdir(CARPETA)
    #validar que sea archivos txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    
    for archivo in archivos_txt:
        with open(CARPETA + archivo)as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')
            
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    
    #Revisar si contacto ya existe antes de editarlo
    existe=existe_contacto(nombre_anterior)
    
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            
           #Resto de los campos
            nombre_contacto =input('Agrega el nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo Telefono: \r\n')
            categoria_contacto=input('Agrega la nueva Categoria: \r\n')
            
            #instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            #escribir archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n' )
            archivo.write('Telefono:' + contacto.telefono + '\r\n' )
            archivo.write('Categoria:' + contacto.categoria + '\r\n' )
            
                        
            #Renombrar el Archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
            #mostrar mensaje de exito
        print('\r\n Contacto Editado Correctamente \r\n')
                  
    else:
        print('Ese contacto no existe!!!') 
    app()   
            
def agregar_contacto():
    print('Escribe los datos para agregar contacto')
    nombre_contacto =input('Nombre del contacto: \r\n')
    
    #revisar si el archivo ya existe antes de crearlo
    existe=existe_contacto(nombre_contacto)
    
    if not existe:
        
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
        
        #resto de los campos
        
            telefono_contacto = input('Agrega el telefono: \r\n')
            categoria_contacto=input('Categoria Contacto: \r\n')
        
        #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
        
        #escribir archivo
            archivo.write('Nombre:' + contacto.nombre + '\n' )
            archivo.write('Telefono:' + contacto.telefono + '\n' )
            archivo.write('Categoria:' + contacto.categoria + '\n' )
        
        #mostar un mesaje de exito
            print('\r\nContacto creado correctamente\r\n')
    else:
        print('\r\nEse contacto ya existe!!!\r\n')    
    
    #reiniciar la app
    app()
#muestra el menu de opciones   
def mostrar_menu():
    
    print('\r\nSeleccione del menu las opciones')
    print('Pulse el numero de la opcion')
    print('1.) Agregar nuevo contacto')
    print('2.) Editar Contacto')
    print('3.) Ver contactos')   
    print('4.) Buscar contacto')
    print('5.) Eliminar contacto')
def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
    
  
    
app()
    
    

