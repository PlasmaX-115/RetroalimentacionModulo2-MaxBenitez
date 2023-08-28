# Momento de Retroalimentación: Módulo 2 Implementación de una técnica de aprendizaje máquina sin el uso de un framework. (Portafolio Implementación)
## Maximiliano Benítez Ahumada - A01752791

Para la realización de esta actividad se implementó el algoritmo KNN para clasificación.

# Manual de Instalación y Configuración de Miniconda y Entorno Virtual con scikit-learn

En este manual, te guiaré a través de los pasos para instalar Miniconda, una versión minimalista de Anaconda, y cómo crear un entorno virtual utilizando Miniconda para trabajar con scikit-learn, una biblioteca de aprendizaje automático en Python.

## Paso 1: Descargar Miniconda

1. Accede al sitio web de Miniconda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

2. Selecciona la versión de Miniconda adecuada para tu sistema operativo (Windows, macOS o Linux).

3. Descarga el instalador y sigue las instrucciones de instalación según tu sistema operativo.

## Paso 2: Instalar Miniconda

### Windows

1. Ejecuta el instalador descargado.

2. Acepta los términos y condiciones.

3. Elige la opción "Instalar solo para mí" y selecciona una ubicación para la instalación (por defecto, `C:\Users\<TuUsuario>\Miniconda3`).

4. Selecciona "Agregar Anaconda a mi PATH" durante la instalación.

5. Haz clic en "Instalar".

### macOS y Linux

1. Abre una terminal.

2. Navega hacia la ubicación del instalador descargado (usando el comando `cd`).

3. Ejecuta el comando de instalación: 

   ```
   bash Miniconda3-latest-MacOSX-x86_64.sh
   ```

   (El nombre del archivo puede variar según la versión descargada).

4. Acepta los términos y condiciones.

5. Sigue las instrucciones en pantalla y proporciona una ubicación para la instalación (por defecto, en tu directorio de inicio).

6. Acepta agregar el inicio de Miniconda al archivo `.bashrc` o `.zshrc` si se te pregunta.

## Paso 3: Crear un entorno virtual con scikit-learn

1. Abre una nueva terminal (si no tienes una abierta).

2. Crea un nuevo entorno virtual con el nombre "sklearn-env" y la versión de Python deseada (por ejemplo, Python 3.8):

   ```
   conda create -n sklearn-env python=3.8
   ```

3. Activa el entorno virtual:

   - En Windows:

     ```
     conda activate sklearn-env
     ```

   - En macOS y Linux:

     ```
     source activate sklearn-env
     ```

4. Instala scikit-learn en el entorno virtual:

   ```
   conda install scikit-learn
   ```

5. ¡Listo! Ahora tienes un entorno virtual con Miniconda y scikit-learn instalados.

## Paso 4: Usar el entorno virtual

1. Cada vez que quieras trabajar con scikit-learn, activa el entorno virtual:

   - En Windows:

     ```
     conda activate sklearn-env
     ```

   - En macOS y Linux:

     ```
     source activate sklearn-env
     ```

2. Cuando hayas terminado de trabajar, desactiva el entorno virtual:

   ```
   conda deactivate
   ```

## Conclusión

¡Has completado la instalación de Miniconda, la creación de un entorno virtual y la instalación de scikit-learn! Ahora estás listo para desarrollar aplicaciones de aprendizaje automático utilizando scikit-learn en un entorno virtual aislado. Recuerda activar el entorno virtual siempre que quieras trabajar con tu proyecto y desactívalo cuando hayas terminado para evitar conflictos entre paquetes. ¡Feliz programación! 🚀
