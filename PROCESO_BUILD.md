# Proceso de distribución y publicación de la tienda

Este documento sirve como bitácora para construir el paquete Python, comprobarlo instalado fuera del código fuente y revisar el build de GitHub Actions. Completa la fecha, los resultados y las capturas en cada etapa. Las capturas deben mostrar la terminal o GitHub con suficiente contexto para identificar el comando, el resultado y el repositorio.

## Datos de la práctica

- Repositorio de GitHub: ______________________________
- Rama de trabajo: ______________________________
- Fecha de ejecución: ______________________________
- Versión del paquete: `1.0.0`
- Python usado localmente: ______________________________

## 1. Preparación y pruebas del proyecto

El paquete se encuentra en `src/devops_tienda`. Su configuración está en `pyproject.toml`; la interfaz de consola se instala como `devops-tienda`. Los scripts y pruebas que ya estaban en la raíz se conservan.

Desde la raíz del repositorio, en PowerShell, ejecutar:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[test]" build
.\.venv\Scripts\python.exe -m pytest -v
```

**Comprobación:** pytest debe terminar con código de salida 0 y mostrar todas las pruebas aprobadas. Si hay fallos, anota el nombre de la prueba y el mensaje antes de continuar.

**Captura 1:** terminal con el comando `python -m pytest -v` (o el ejecutable del entorno virtual) y el resumen final de pruebas aprobadas. No cortes el resultado ni ocultes los fallos.

- Resultado / observaciones: ____________________________________________
- Nombre de captura: `01-pruebas.png`

## 2. Construcción de la distribución

Construir wheel y distribución de código fuente:

```powershell
.\.venv\Scripts\python.exe -m build
Get-ChildItem .\dist
```

**Comprobación:** `dist` debe contener un archivo `.whl` y otro `.tar.gz`, ambos con nombre y versión `devops_tienda-1.0.0`.

**Captura 2:** terminal mostrando `python -m build` finalizado correctamente y el listado de los dos archivos dentro de `dist`.

- Resultado / observaciones: ____________________________________________
- Nombre de captura: `02-build-local.png`

## 3. Instalación y validación del wheel

Crear un entorno aislado e instalar el wheel recién generado:

```powershell
py -m venv .venv-build
.\.venv-build\Scripts\python.exe -m pip install .\dist\devops_tienda-1.0.0-py3-none-any.whl
@("200", "25") | .\.venv-build\Scripts\devops-tienda.exe
.\.venv-build\Scripts\python.exe -c "from devops_tienda.tienda import calcular_precio, calcular_iva; assert calcular_precio(200,25) == 150; assert calcular_iva(100) == 116; print('Validación correcta')"
```

**Comprobación:** la importación y las aserciones deben pasar; para precio 200 y descuento 25, la consola debe mostrar total con IVA de `$174.00`. El comando se ejecuta desde el entorno instalado, no desde `python tienda.py`.

**Captura 3:** terminal con la instalación del wheel, el cálculo de comprobación y la salida `Total con IVA: $174.00`.

- Resultado / observaciones: ____________________________________________
- Nombre de captura: `03-wheel-instalado.png`

## 4. Build automatizado en GitHub Actions

El workflow `.github/workflows/build.yml` se ejecuta en `push`, `pull_request` y manualmente. El job `build` instala dependencias, corre las pruebas, genera las distribuciones y publica `paquete-tienda` como artefacto. El job `verificar` descarga ese artefacto, instala el wheel y comprueba las funciones y el comando de consola.

Después de subir los cambios al repositorio, abrir **GitHub → Actions → Build Python package** y seleccionar la ejecución más reciente.

**Comprobación:** los jobs `build` y `verificar` deben estar en verde. En `build`, revisar las etapas de pruebas y construcción. En `verificar`, revisar la instalación del wheel y el comando de consola. Confirmar que el resumen ofrece el artefacto `paquete-tienda`.

**Captura 4:** página del run con ambos jobs aprobados y el artefacto visible. Si un job falla, captura también el paso expandido con el error.

- URL o identificador de la ejecución: __________________________________
- Resultado / observaciones: ____________________________________________
- Nombre de captura: `04-actions-ok.png`

## 5. Publicación de cambios y comprobación final

Esta carpeta de trabajo no contiene una carpeta `.git`, así que todavía no está enlazada a GitHub. Primero abre o clona el repositorio real en una carpeta de trabajo y lleva allí los archivos de esta práctica. No ejecutes `git add` desde una carpeta que no sea la copia enlazada al repositorio correcto. En esa copia, confirma el remoto y la rama:

```powershell
git remote -v
git branch --show-current
git status --short
git diff --check
```

Si `git remote -v` no muestra el repositorio esperado, detente y configura/abre la copia correcta antes de publicar. Cuando el remoto sea correcto y la revisión no muestre errores, guardar y subir los cambios:

```powershell
git add .
git commit -m "Agregar build y distribución del paquete Python"
git push
```

**Comprobación:** en GitHub, abrir el commit y confirmar que aparecen los archivos de empaquetado y `.github/workflows/build.yml`. Luego volver a **Actions** y verificar que el run asociado a ese commit termina con ambos jobs aprobados. No considerar publicado correctamente hasta comprobar el resultado remoto.

**Captura 5:** página del commit con su identificador y archivos cambiados. **Captura 6:** ejecución de Actions asociada a ese commit con los dos jobs aprobados.

- Identificador del commit: _____________________________________________
- URL del commit: ______________________________________________________
- URL del run de Actions: ______________________________________________
- Resultado final: _____________________________________________________

## Registro de incidencias

| Etapa | Incidencia o mensaje | Corrección aplicada | Resultado |
|---|---|---|---|
| Pruebas | | | |
| Build local | | | |
| Instalación del wheel | | | |
| GitHub Actions | | | |
| Publicación | | | |

