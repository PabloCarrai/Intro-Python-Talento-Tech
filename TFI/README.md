# Trabajo Final Integrador(Gestor Productos)

_Proyecto final del curso introduccion a Python - Full Stack Talento Tech_

### Pre-requisitos 📋

_Necesitas tener python instalado y generarte un entorno virtual_

```
python3 -m venv venv
source venv/bin/activate
```

### Instalación 🔧

_Una vez instalado python y generado el entorno virtual tendras que instalar los modulos usados con_


```
pip install -r requirements.txt
```

## Ejecutando las pruebas ⚙️

_La primer vez que ejecutes el programa puede ocurrir que te traigas todos los archivos necesarios, o en su defecto te falte el archivo que contiene la base de datos en sqlite3. Si viene con el archivo, es muy probable que contenga registros que no te interece conservar. Corriendo el programa en el primer menu tenes una opcion referente al manejo de la base de datos. Este es la opcion 1. En esta opcion podras inicializar desde cero este archivo. Primero seria elegir la opcion de eliminar el archivo, para poder arrancar desde cero. Luego inicializar, con esto te garantizas iniciar con una base de datos vacia pero funcional._

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Python](https://docs.python.org/3/) - Lenguaje con el que programamos
* [Sqlite](https://sqlite.org/docs.html) - Gestor de bases de datos locales


## Checklist de objetivos 
### Funcionalidades
- ✅ Registrar nuevos Productos.
- ✅ Visualizar datos de los Productos Registrados
- ✅ Actualizar datos del Producto, mediante Id.
- ✅ Eliminacion de Productos, mediante su Id
- ✅ Busqueda de Productos, mediante su Id. De manera opcional, se puede implementar la busqueda por los campos nombre o categoria.
- ✅ Reporte de Productos que tengan una cantidad igual o inferior a un limite especificado por el Usuario/a

### Base de Datos
_Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos.La tabla 'productos debe contener las siguientes columnas'_

```
id: Identificador unico del producto(clave primaria,autoincremental)
nombre: Nombre del producto(texto, no nulo)
descripcion: Breve descripcion del producto(texto)
cantidad: Cantidad disponible del producto(entero, no nulo)
precio: Precio del producto(real, no nulo)
categoria: Categoria a la que pertenece el producto(texto)
```

### Interfaz de Usuario
_Implementar una interfaz de usuario basica, para interactuar con la base de datos a traves de la terminal. La intergaz debe incluir un menu principal con las opciones necesarias para acceder a cada funcion descrita anteriormente._

### Opcional
_Utilizar el modulo colorama para mejorar la legibilidad y experiencia de usuario en la termina, añadiendo colores a los mensajes y opciones. El codigo debe estar bien estructurado, utilizando funciones para modularizar la logica de la aplicacion. Los comentarios deben estar presentes en el codigo, explicando las partes claves del mismo_

### Flujo de la aplicacion. 
_La aplicacion corre particularmente desde el archivo main.py. El mismo tiene el punto de arranque de la aplicacion. Desde aca llamamos a un modulo que tiene el menu propiamente de la aplicacion este modulo se encuentra en el archivo cli.py. Dicho modulo muestra las diferentes opciones, y dependiendo de los datos ingresados se vale del archivo funciones_extras.py que contiene funciones con funcionalidades particulades como validaciones entre otras funciones. Luego para el caso de tener que hacer algo con respecto a la base de datos el modulo se comunica con las funciones creadas en el archivo db.py. Que contiene muchas funciones para realizar esas tareas_

### Desarrollador 🙋🏻‍♂️
Pablo Carrai
- Correo: [pablohernanjuan@hotmail.com](mailto:pablohernanjuan@hotmail.com)
- Repositorio [github.com/PabloCarrai:](https://github.com/PabloCarrai)