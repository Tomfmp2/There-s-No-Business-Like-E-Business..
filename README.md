# Autores

### Manuel Lahitton (Scrum Master)    👨🏻‍💼
### Alejandro Escobar (Product Owner) 👩🏽‍💼
### Sahiam Esteban
### Tomas Medina
### Nicolas Zabala

- Grupo J1
- Campuslands


# Proyecto There's No Business Like E-Business 💻

### Este proyecto consiste en el desarrollo de un sistema de comercio electrónico en Python, diseñado para ofrecer una gestión integral de productos, ventas y pagos. El sistema cuenta con dos vistas principales:

## Vista del usuario

 - 🔹📖 Permite visualizar los productos disponibles organizados por tienda.
 - 🔹🛒 Posibilidad de añadir productos al carrito de compras.
 - 🔹💳 Procesar pagos a través de diferentes métodos: tarjeta de crédito, tarjeta débito, PSE, entre otros.

## Vista del dueño/administrador

 🔹 🗂️ Administración completa del inventario (agregar, actualizar o eliminar productos).

 🔹 📖 Visualización de las ventas realizadas.

 🔹 📙 Control de la información almacenada en el sistema.

## 🚀 Características principales

 - 💾 Almacenamiento en JSON: toda la información de productos, usuarios y transacciones se guarda en archivos JSON para mantener persistencia de datos.
 - 💻 Gestión por menús interactivos: la navegación se realiza mediante menús dinámicos e intuitivos.
 - 🗽 Soporte multilenguaje: el sistema puede ejecutarse en español o inglés, adaptándose a las necesidades del usuario.
 - 👥 Sistema de Login y sesiones
 - 📒 Administracion de Productos
 - ✏️ Editar o eliminar productos

 ## - 🛠️ Stack tecnologico

 - **Python 3.0**
 - **Json**

 ## - Requerimientos

 **Sistema operativo** windows o linux
 - **Python** version 3 o superior

 ## ▶️ Ejecución:

    - En windows:
            1. Abrir la terminal de windows.
            2. Navegar a la carpeta donde está el archivo:
            cd ruta/del/proyecto
    
    - En linux:
            1. abrir una terminal
            2. buscar el archivo
            cd ruta/del/proyecto

## 📚 Librerias utilizadas:

os, json, time

# Documentación del Proyecto Scrum

## 1. Visión del Proyecto

**Nombre del Proyecto:** No hay comercio como el comercio electrónico **Descripción:** Desarrollo de una plataforma para ayudar a pequeños negocios a montar tiendas en línea fácilmente, permitiendo vender a clientes sin necesidad de conocimientos técnicos avanzados, cumpliendo con estándares empresariales sólidos. **Objetivo:** Crear una herramienta intuitiva que permita a pequeños negocios crecer mediante ventas en línea, con soporte para múltiples usuarios, pagos seguros y administración mínima. **Stakeholders:** Dueños de pequeños negocios (clientes), Empresa desarrolladora, Usuarios finales (compradores).

## 2. Roles y Responsabilidades

**Product Owner:** [Jhon Alejandro Escobar Lozada] - Define y prioriza el Product Backlog, asegura que el producto cumpla con los requisitos del cliente.

**Scrum Master:** [Manuel Jose Gomez Lahitton] - Facilita las ceremonias Scrum, elimina impedimentos y fomenta las buenas prácticas.

**Equipo de Desarrollo:** [Sahiam Valentina Esteban Esteban, Nicolas Zabala Castañeda, Tomas Medina Prada] - Responsable de diseñar, desarrollar y probar el incremento.

## 3. Product Backlog

**Notas:** El Product Backlog se actualiza después de cada Sprint Review. Prioridades revisadas por el Product Owner en colaboración con los stakeholders.

- **US1 - Registro de usuario** (5 puntos)
  - Descripción: Como cliente, quiero registrarme con un correo y contraseña, para poder acceder a la plataforma.
  - Criterios de aceptación:
    - Se desarrolla una función que permita registrar un usuario con correo y contraseña, y los datos deben guardarse en un archivo JSON.
    - Si el correo ya existe en el archivo JSON, el sistema debe rechazar el registro y mostrar un mensaje de error ("El correo ya está registrado").
    - Si el registro es exitoso, el sistema debe mostrar un mensaje de confirmación ("Usuario registrado con éxito").
- **US2 - Inicio de Sesión (Usuario)** (3 puntos)
  - Descripción: Como cliente, quiero iniciar sesión con mis credenciales, para acceder a mi cuenta.
  - Criterios de aceptación:
    - Se desarrolla una lógica que revise los datos de ingreso de sesión y los compare con los existentes en el archivo JSON (el sistema compara correo y contraseña con lo guardado en JSON).
    - Si las credenciales son correctas, se debe mostrar un mensaje: "Inicio de sesión exitoso".
    - Si las credenciales son incorrectas, se debe mostrar un mensaje de error: "Usuario o contraseña incorrectos".
    - Si la credencial de usuario no existe, se debe mostrar un mensaje de error: "Usuario no encontrado en el sistema".
- **US3 - Inicio de Sesión (Dueño)** (2 puntos)
  - Descripción: Como dueño del negocio, quiero iniciar sesión con mis credenciales, para acceder a mi cuenta de administrador.
  - Criterios de aceptación:
    - El sistema compara correo y contraseña con lo guardado en JSON.
    - Si coinciden, acceso exitoso.
    - Si no coinciden, muestra error.
- **US4 - Vista de página (Usuario)** (5 puntos)
  - Descripción: Como usuario, quiero tener una vista que permita visualizar los productos disponibles, para poder escoger de manera fácil el producto que quiero agregar al carrito.
  - Criterios de aceptación:
    - Se visualizan los productos.
    - Se ordenen alfabéticamente.
- **US5 - Vista de página (Dueño)** (8 puntos)
  - Descripción: Como dueño del negocio, quiero ver los objetos que tengo disponibles, para poder gestionarlos a mi conveniencia.
  - Criterios de aceptación:
    - Se ingresa a una vista de administrador.
- **US6 - Agregar Producto** (5 puntos)
  - Descripción: Como dueño de negocio, quiero registrar productos con nombre, precio y categoría, para poder venderlos.
  - Criterios de aceptación:
    - Se desarrolla una función que permita ingresar un producto con nombre, precio y categoría, y guardarlo en un archivo JSON.
    - Se crea una lógica que permita validar los nombres de los productos para verificar que el que se quiere agregar no exista de antemano en el archivo JSON.
    - Se valida que el precio ingresado sea mayor a 0.
    - Si el registro es exitoso, el sistema debe mostrar el mensaje: "Producto agregado con éxito".
- **US7 - Editar o eliminar producto** (5 puntos)
  - Descripción: Como dueño de negocio, quiero editar o eliminar productos existentes, para mantener mi catálogo actualizado.
  - Criterios de aceptación:
    - Se diseña una interfaz que permita filtrar los productos por nombre (Se puede buscar un producto por nombre).
    - Se permite modificar los parámetros de precio y categoría del producto seleccionado.
    - Se debe permitir eliminar el producto de forma permanente y que no aparezca en el listado.
    - Si el producto no existe, el sistema debe mostrar el mensaje de error: "El producto no fue encontrado".
- **US8 - Agregar al carrito** (2 puntos)
  - Descripción: Como cliente, quiero agregar productos al carrito, para comprarlos después.
  - Criterios de aceptación:
    - El sistema permite elegir un producto existente y añadirlo al carrito de compras.
    - Si el producto ya existe en el carrito de compras y se vuelve a seleccionar, debe aumentar la cantidad en vez de duplicarse.
    - El carrito debe guardarse en el archivo JSON y mostrar un mensaje que diga "Producto agregado al carrito".
- **US9 - Quitar del carrito** (3 puntos)
  - Descripción: Como cliente, quiero eliminar productos del carrito, para no pagarlos.
  - Criterios de aceptación:
    - El sistema debe permitir seleccionar un producto dentro del carrito y eliminarlo.
    - Si el producto no existe en el carrito, se debe mostrar un mensaje de error: "El producto no está en el carrito".
    - El carrito debe actualizarse en un diccionario o JSON después de la eliminación.
    - Debe mostrarse un mensaje de confirmación: "Producto eliminado del carrito".
- **US10 - Sistema de pagos** (13 puntos)
  - Descripción: Como cliente, quiero poder elegir como realizar el pago (Ya sea tarjeta de crédito con selección a cuotas, tarjeta débito o contrarentrega), para finalizar mi compra.
  - Criterios de aceptación:
    - El sistema debe calcular el total del carrito antes del pago.
    - El sistema debe permitir elegir un método de pago (ejemplo: tarjeta o débito).
    - Una vez confirmado, el carrito debe vaciarse automáticamente.
    - Debe mostrarse un mensaje final: "Compra realizada con éxito".
- **US11 - Internacionalización** (5 puntos)
  - Descripción: Como cliente, quiero elegir entre español o inglés, para usar la plataforma en mi idioma.
  - Criterios de aceptación:
    - Se puede seleccionar idioma al inicio.
    - Los mensajes del sistema cambian según idioma.

## 4. Sprint Backlog

**Sprint 1:** [1 - agosto] - [16 - agosto]

**Objetivo del Sprint:** Implementar funcionalidades básicas de la plataforma de comercio electrónico, incluyendo soporte para usuarios y pagos iniciales.

**Tareas del Sprint 1:**

| Tarea                                          | Estado | User Story                                  |
| ---------------------------------------------- | ------ | ------------------------------------------- |
| Diseñar formulario de registro                 | Done   | US1 - Registro de usuario (5 puntos)        |
| Implementar validación de credenciales         | Done   | US1 - Registro de usuario (5 puntos)        |
| Crear archivo JSON para usuarios               | Done   | US1 - Registro de usuario (5 puntos)        |
| Diseñar formulario de inicio de sesión         | Done   | US2 - Inicio de Sesión (Usuario) (3 puntos) |
| Implementar lógica de comparación con JSON     | Done   | US2 - Inicio de Sesión (Usuario) (3 puntos) |
| Adaptar formulario para administrador          | Done   | US3 - Inicio de Sesión (Dueño) (2 puntos)   |
| Implementar validación para administrador      | Done   | US3 - Inicio de Sesión (Dueño) (2 puntos)   |
| Diseñar interfaz de visualización de productos | Done   | US4 - Vista de página (Usuario) (5 puntos)  |
| Implementar ordenamiento alfabético            | Done   | US4 - Vista de página (Usuario) (5 puntos)  |
| Conectar datos de productos                    | Done   | US4 - Vista de página (Usuario) (5 puntos)  |
| Asegurar funcionalidad de agregar al carrito   | Done   | US4 - Vista de página (Usuario) (5 puntos)  |

**Sprint 2:** [18 - agosto] - [1 - septiembre]

**Objetivo del Sprint:** Ampliar la funcionalidad de la plataforma con gestión de productos, carrito de compras y proceso de pago.

**Notas:** Durante este sprint, se enfrentó un problema crítico cuando un programador eliminó accidentalmente la base de datos, lo que causó un retraso significativo en el progreso. Como resultado, solo se completaron US5, US6 y US8, mientras que US7 quedó en progreso y no se pudo entregar.

**Tareas del Sprint 2:**

| Tarea                                                 | Estado      | User Story                                  |
| ----------------------------------------------------- | ----------- | ------------------------------------------- |
| Diseñar interfaz para agregar productos               | Done        | US5 - Vista de página (Dueño) (8 puntos)    |
| Implementar funcionalidad de edición de productos     | Done        | US7 - Editar o eliminar producto (5 puntos) |
| Desarrollar eliminación de productos con confirmación | Done        | US7 - Editar o eliminar producto (5 puntos) |
| Guardar cambios de productos en JSON                  | Done        | US6 - Agregar producto (5 puntos)           |
| Implementar botón "Agregar al carrito"                | Done        | US8 - Agregar al carrito (2 puntos)         |
| Almacenar productos en lista de carrito               | Done        | US8 - Agregar al carrito (2 puntos)         |
| Mostrar contador de ítems en carrito                  | Done        | US8 - Agregar al carrito (2 puntos)         |
| Diseñar página de vista del carrito                   | In Progress | US7 - Editar o eliminar producto (5 puntos) |
| Implementar ajuste de cantidad de productos           | In Progress | US7 - Editar o eliminar producto (5 puntos) |
| Habilitar eliminación de ítems del carrito            | In Progress | US7 - Editar o eliminar producto (5 puntos) |
| Calcular y mostrar total a pagar                      | In Progress | US7 - Editar o eliminar producto (5 puntos) |

**Sprint 3:** [2 - septiembre] - [15 - septiembre]

**Objetivo del Sprint:** Finalizar el carrito de compras y agregar funcionalidades de pagos, internacionalización y eliminación de productos del carrito.

**Tareas del Sprint 3:**

| Tarea                                                     | Estado | User Story                                  |
| --------------------------------------------------------- | ------ | ------------------------------------------- |
| Finalizar página de vista del carrito                     | Done   | US7 - Editar o eliminar producto (5 puntos) |
| Finalizar ajuste de cantidad de productos                 | Done   | US7 - Editar o eliminar producto (5 puntos) |
| Finalizar eliminación de ítems del carrito                | Done   | US7 - Editar o eliminar producto (5 puntos) |
| Finalizar cálculo y mostrar total a pagar                 | Done   | US7 - Editar o eliminar producto (5 puntos) |
| Permitir selección de producto en el carrito y eliminarlo | Done   | US9 - Quitar del carrito (3 puntos)         |
| Mostrar mensaje de error si no existe                     | Done   | US9 - Quitar del carrito (3 puntos)         |
| Actualizar diccionario o JSON después de eliminación      | Done   | US9 - Quitar del carrito (3 puntos)         |
| Mostrar mensaje de confirmación                           | Done   | US9 - Quitar del carrito (3 puntos)         |
| Calcular total del carrito antes del pago                 | Done   | US10 - Sistema de pagos (13 puntos)         |
| Permitir elegir método de pago                            | Done   | US10 - Sistema de pagos (13 puntos)         |
| Vaciar carrito al confirmar                               | Done   | US10 - Sistema de pagos (13 puntos)         |
| Mostrar mensaje final                                     | Done   | US10 - Sistema de pagos (13 puntos)         |
| Permitir selección de idioma al inicio                    | Done   | US11 - Internacionalización (5 puntos)      |
| Cambiar mensajes según idioma                             | Done   | US11 - Internacionalización (5 puntos)      |

## 5. Ceremonias

**Sprint Planning:** Cada 2 semanas. Objetivo: Seleccionar ítems del Product Backlog y planificar el Sprint Backlog.

**Daily Scrum:** 10:00 AM, reunión presencial. Formato: Cada miembro responde: ¿Qué hice ayer? ¿Qué haré hoy? ¿Algún impedimento?

**Sprint Review:** Al final de cada sprint, 1 hora. Participantes: Equipo Scrum, stakeholders. Entregables: Demostración del incremento y retroalimentación.

**Sprint Retrospective:** Al final de cada sprint, 1 hora. Objetivo: Identificar qué funcionó, qué no y cómo mejorar en el próximo sprint.

## 6. Métricas

##### **Sprint 1:**

![Sprint 1 chart](https://cdn.discordapp.com/attachments/1410318821318987816/1417365956237197353/chart.png?ex=68ca3869&is=68c8e6e9&hm=d29894adadd970d91db6db95792ef59edc7919253d50c5a8c71f98f677128f44&)

**Impedimentos Resueltos:** [0 impedimentos resueltos en el Sprint 1].

**Velocity:** [15 puntos].

##### **sprint 2:**

![sprint2](https://cdn.discordapp.com/attachments/1410318821318987816/1417365812901314632/chart.png?ex=68ca3847&is=68c8e6c7&hm=fee7f975d175318f6d82ad150770ddbd6106638eddba6033f3b6388d9c26b88e&)

**Impedimentos Resueltos:** [1 Impedimento Resuelto en el sprint 2]

**Velocity:** [20 puntos]

**sprint 3:**

![sprint 3](https://cdn.discordapp.com/attachments/1410318821318987816/1417365659482062939/chart.png?ex=68ca3822&is=68c8e6a2&hm=27684df4d901cfa406495926db068e4061194b3e70b9b115b1f47d6cca4833dd&)

**Impedimentos Resueltos:** [0 Impedimentos Resueltos en el sprint 3]

**Velocity:** [20 puntos]

## 7. Definición de "Done"

- Código revisado por pares.
- Pruebas unitarias aprobadas.
- Documentación actualizada.
- Incremento funcional y desplegado en el entorno de prueba.

## 8. Riesgos e Impedimentos

| Riesgo/Impedimento                                | Mitigación                                                   | Estado   |
| ------------------------------------------------- | ------------------------------------------------------------ | -------- |
| Pérdida accidental de la base de datos (Sprint 2) | Restaurar datos desde copias de seguridad y establecer un protocolo de respaldo; ocurrió el 20 de agosto de 2025 a las 08:55 AM -05 debido a un error humano al manipular el archivo JSON | Resuelto |

## 9. Historial de Sprints

**Sprint 1:** [1 - agosto] - [16 - agosto] - [Todas las tareas se entregaron a tiempo y se completaron exitosamente sin impedimentos].

**Sprint 2:** [1 - septiembre] - [Se completaron US5, US6 y US8, pero US7 quedó en progreso debido a un impedimento registrado (ver sección 8 - Riesgos e Impedimentos)].

**Sprint 3:** [2 - septiembre] - [15 - septiembre] - [Se completaron todas las tareas a tiempo, manteniendo avances durante bastante tiempo].

## 10. Notas Adicionales

El proyecto se gestionó en Trello: [Link Trello](https://trello.com/b/IDjuOxom/there-is-no-commerce-like-e-commerce). [Cualquier información relevante, como enlaces a herramientas, repositorios o documentos relacionados]. Repositorio del backlog: backlog/backlog_sprint_1.md

## 11. Link del video Proyecto Scrum

[**Caso práctico: Scrum en acción**](https://youtu.be/L3XKVNj3ZWk?si=LCk2jvvgWJTpNJ9d)


