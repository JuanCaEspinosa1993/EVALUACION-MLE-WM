# Prediccion de lluvia

Modelo de machine learning que predice si lloverá o no al dia siguiente.

## Estado del Proyecto

[![Estado del Proyecto](https://img.shields.io/badge/estado-en%20desarrollo-yellow)](URL)

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#Estructura-del-proyecto)
- [Deficiencias en notebook original](#Deficiencias-en-notebook-original)
- [Interaccion de estructura de carpetas con ambiente de producción](#DInteraccion-de-estructura-de-carpetas-con-ambiente-de-producción)



## Requisitos

- Python 3.12.4

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/proyecto.git
    ```
2. En la terminal, navegar a la carpeta dle proyecto. Una vez dentro de la carpeta del proyecto crea un ambiente virtual:

    Para windows:
    ```bash
    python -m venv myenv
    ```
    Para Linux
     ```bash
    python3.12 -m venv myenv
    ```
3. Activar entorno virtual.
     Para windows:
    ```bash
    .\myenv\Scripts\activate
    ```
    Para Linux
     ```bash
    source myenv/bin/activate
    ```
4. Instala las dependencias:
    Si es necesatio, actualiza pip

    ```bash
    pip install -r requirements.txt
    ```



## Uso

Ejemplo de cómo usar el proyecto:

```bash
python main.py
```

## Estructura-del-proyecto
En la imagen se muestra la estructura de carpetas usadas en el proyecto
![Estructura del Proyecto](reports/figures/project_structure.png)

## Deficiencias en notebook original

1. Modularización. Un solo notebook para todo el proceso, el mantenimiento para este tipo de archivos es mas dificil por la organización.

2. Exceso de código comentado. Por buenas prácticas se debe mantener solo el código que realmente se usará.

3. Duplicidad de código.Existen lineas de código repetidos que se mejoraron en la parte de src craeando funciones e implementado reusabilidad de código.

4. Nombre de variables. Algunos nombres de variables no proporcionan información respecto a su naturaleza (contexto). Para esto se renombraron variables con la finalidad de mejorar la pertenencia y comprensión de la app.

5. Eficiencia de código. Existen bucles anidados que incrementar la complejidad de los algoritmos. Respecto a esto se crearon estructuras de Comprehension para mejorar el performance.

## Interaccion de estructura de carpetas con ambiente de producción

1. Organización y Mantenimiento
Interacción:

**Facilita el Navegamiento**: Una estructura de carpetas bien organizada permite encontrar y trabajar con archivos de manera más eficiente. Esto **reduce el tiempo dedicado a buscar archivos** y mejora la productividad.

**Simplifica el Mantenimiento**: Una estructura clara facilita la tarea de realizar cambios y actualizaciones en el proyecto, ya que los archivos están organizados de manera lógica y consistente.

2. Escalabilidad.

Facilita la Escalabilidad: A medida que el proyecto crece, una estructura de carpetas bien definida **facilita la integración de nuevos módulos y funcionalidades sin causar desorden**.

Manejo de Dependencias: Permite gestionar las dependencias y configuraciones de manera ordenada, **reduciendo conflictos y problemas en el entorno de producción.**

3. Despliegue y Automatización
Interacción:

Facilita el Despliegue: Permite crear scripts de despliegue que copian solo los archivos necesarios al entorno de producción. Esto asegura que el entorno de producción esté limpio y libre de archivos innecesarios.

4. Colaboración.

Facilita la colaboración entre diferentes miembros del equipo.

5. Documentación y Versionado.

Facilita la Documentación: En el readme.md se explica la replicación del proyecto para su correcta instalación.

Versionado: Se usa git para control de versiones de códigon. con ayuda de **.gitignore** eliminamos posibilidad de subir documentos confidenciales.