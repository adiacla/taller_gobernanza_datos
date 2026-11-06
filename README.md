# Auditoría de Calidad de Datos (ISO 5259) - SaluCompleta

Este repositorio contiene el framework y los artefactos para la evaluación y auditoría de la calidad de los conjuntos de datos de **SaluCompleta**, estructurado bajo el estándar internacional **ISO 5259** (Calidad de datos para Analítica e Inteligencia Artificial). 

El proyecto utiliza **DVC (Data Version Control)** para la gestión y el versionamiento de los datasets (`.csv`) sin saturar el historial de Git, garantizando la reproducibilidad del pipeline de datos.

---

##  Objetivo del Repositorio
El objetivo principal es implementar un proceso sistemático de auditoría que mida, valide y documente las dimensiones de calidad de los datos de los pacientes (versiones v1 y v2), asegurando que los datos cumplan con los requisitos normativos antes de su uso en modelos analíticos o de toma de decisiones.

---

##  Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
*   [Python 3.10+](https://python.org)
*   [Git](https://git-scm.com)
*   [Visual Studio Code (VS Code)](https://visualstudio.com)

---

##  Instrucciones de Uso en VS Code

Sigue estos pasos detallados para clonar, configurar y ejecutar el entorno de desarrollo directamente en Visual Studio Code.

### 1. Clonar el Repositorio e Iniciar VS Code
Abre tu terminal y ejecuta:
```bash
git clone <URL_DE_TU_REPOSITORIO_GITHUB>
cd <NOMBRE_DE_LA_CARPETA>
code .
```
*(Esto abrirá automáticamente la carpeta del proyecto en una nueva ventana de VS Code).*

### 2. Configurar el Entorno Virtual (venv)
Abre la terminal integrada de VS Code (`Ctrl + Shift + \`` o `Cmd + Shift + \`` en Mac) y ejecuta:

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar la Extensión Recomendada en VS Code
Para gestionar los datos y experimentos de forma visual dentro del entorno, instala la siguiente extensión desde el Marketplace de VS Code (`Ctrl + Shift + X`):
*   **DVC Extension Pack** (de lakeFS) - *Instala el entorno completo: DVC para VS Code, soporte de autocompletado YAML para pipelines y herramientas esenciales de Python.*

### 4. Instalar las Dependencias
Con el entorno virtual activado en tu terminal de VS Code, instala las librerías necesarias:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Descargar los Datos con DVC
El repositorio no incluye los archivos `.csv` pesados por defecto, solo sus punteros `.dvc`. Para traer los datos reales a tu entorno local, ejecuta:
```bash
dvc pull
```
*(Nota: Asegúrate de tener configuradas las credenciales de acceso al almacenamiento remoto de DVC).*

---

##  Estructura Principal del Proyecto

*   `Auditoria_Dataset_SaluCompleta_ISO5259.ipynb`: Notebook de Jupyter con el análisis de calidad de datos paso a paso.
*   `Auditoria_Dataset_SaluCompleta_ISO5259.pptx`: Presentación ejecutiva con las conclusiones y métricas de la auditoría.
*   `remediar_dataset.py`: Script de Python con funciones auxiliares para la limpieza o transformación de datos.
*   `pacientes_salucompleta_v1.csv.dvc`: Archivo de rastreo de DVC para la primera versión del dataset.
*   `dvc.yaml` / `dvc.lock`: Archivos de configuración del pipeline de DVC.
