# Proyecto FastAPI - miguel

## Información del Aprendiz

* Nombre: Miguel Caballero
* Programa: ADSO
* Tecnología utilizada:

  * Python
  * FastAPI
  * Git
  * GitHub

---

# Descripción del Proyecto

Este proyecto consiste en la creación de una API utilizando FastAPI.

La aplicación permite ejecutar un servidor local y crear endpoints para responder solicitudes HTTP.

---

# Creación del Entorno Virtual

Se creó un entorno virtual para aislar las dependencias del proyecto.

Comando utilizado:

```bash
python3 -m venv .mi_env
```

Activación del entorno virtual en Git Bash:

```bash
source .mi_env/Scripts/activate
```

Cuando el entorno está activo aparece:

```bash
(.mi_env)
```

---

# Instalación de FastAPI

Comando utilizado:

```bash
pip install "fastapi[standard]"
```

Descripción:
Se instaló FastAPI junto con sus dependencias necesarias para el desarrollo.

---

# Archivo Principal

Archivo creado:

```bash
main.py
```

---

# Código Principal

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo"}
```

---

# Ejecución del Servidor

Comando utilizado:

```bash
fastapi dev main.py
```

o también:

```bash
uvicorn main:app --reload
```

---

# Endpoint Principal

Ruta:

```bash
/
```

Respuesta esperada:

```json
{
  "mensaje": "Hola mundo"
}
```

---

# Pruebas del Proyecto

Abrir en el navegador:

```bash
http://127.0.0.1:8000
```

Documentación automática de FastAPI:

```bash
http://127.0.0.1:8000/docs
```

---

# Comandos Git Utilizados

## Inicializar repositorio

```bash
git init
```

## Verificar estado

```bash
git status
```

## Agregar archivos

```bash
git add .
```

## Crear commit

```bash
git commit -m "Nuevo proyecto FastAPI"
```

## Subir cambios a GitHub

```bash
git push origin main
```

---

# Archivos del Proyecto

* `main.py`
* `requirements.txt`
* `.gitignore`
* `README.md`

---

# Dependencias

El proyecto utiliza las siguientes dependencias:

* FastAPI
* Uvicorn
* Pydantic

Estas dependencias quedan registradas en:

```bash
requirements.txt
```
