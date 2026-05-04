---

## 📊 JSON utilizado

**Fuente:** `euro_modificado.json`  
**Nombre del torneo:** Euro 2024  
**Total de partidos:** 51

El JSON contiene todos los partidos de la Eurocopa 2024, desde la fase de grupos hasta la final. Cada partido incluye los siguientes campos:

| Campo | Descripción |
| --- | --- |
| `round` | Ronda del torneo (Matchday 1-3, Round of 16, Quarter-finals, Semi-finals, Final) |
| `date` | Fecha del partido |
| `time` | Hora de inicio |
| `team1` / `team2` | Equipos participantes |
| `score` | Resultado al descanso (`ht`) y final (`ft`) |
| `goals1` / `goals2` | Goleadores de cada equipo (nombre, minuto, penalti, autogol) |
| `ground` | Ciudad donde se disputó el partido |
| `group` | Grupo (solo en fase de grupos) |
| `yellow_cards` | Tarjetas amarillas por equipo |

---

## 🚀 Instalación y ejecución local

```bash

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

Abrir en el navegador: http://127.0.0.1:5000

---

## 🌐 Rutas de la aplicación

| Ruta | Descripción |
| --- | --- |
| `/` | Página de inicio con imagen del torneo |
| `/partidos` | Listado y búsqueda de partidos |
| `/partido/<id>` | Detalle completo de un partido |

---

## 🔍 Funcionalidades

- **Búsqueda por equipo** — búsqueda parcial en nombre de equipo local o visitante
- **Filtro por ronda** — selector generado dinámicamente desde el JSON
- **Ordenación por fecha** — ascendente o descendente
- **Vista de detalle** — muestra toda la información del partido: resultado, goleadores, estadio y tarjetas
- **Error 404** — si se accede a un partido inexistente
- **Herencia de plantillas** — todas las páginas extienden `base.html`

---

## ☁️ Despliegue en Railway

La aplicación está desplegada en [Railway](https://railway.app), una plataforma PaaS que permite desplegar apps directamente desde GitHub.

**URL de producción:** https://flask-eurocopa-gmo.up.railway.app/

El despliegue es automático: cada `git push` a `main` redespliega la aplicación.

Archivos necesarios para el despliegue:
- `requirements.txt` — dependencias del proyecto
- `Procfile` — indica a Railway cómo arrancar la app (`web: gunicorn app:app`)

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Flask
- Jinja2
- HTML5 + CSS3
- Railway (despliegue)