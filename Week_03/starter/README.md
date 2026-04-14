# 🌱 Agrotech API - Plataforma de Maquinaria Agrícola

API desarrollada con FastAPI para gestionar un catálogo de maquinaria agrícola con búsqueda avanzada y múltiples filtros.

---

## 🚜 Dominio

**Agrotech - Plataforma de Maquinaria Agrícola**

Este sistema permite gestionar maquinaria como tractores, cosechadoras y equipos agrícolas, permitiendo filtrarlos por diferentes criterios relevantes del negocio.

---

## 🧱 Estructura del Proyecto

starter/
├── main.py
├── database.py
├── models/
│ ├── category.py
│ └── entity.py
├── schemas/
│ └── filters.py
├── routers/
│ ├── categories.py
│ └── entities.py
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## 📦 Entidades

### 📁 Categorías (MachineryCategory)

- id
- code
- name
- description
- requires_operator

---

### 🚜 Maquinaria (Machinery)

- id
- sku
- name
- category_id
- brand
- model
- year
- price_per_day
- availability

---

## 🔎 Filtros Disponibles

La API permite aplicar múltiples filtros:

- `brand`
- `price_gte`
- `price_lte`
- `year_gte`
- `availability`
- `search` (nombre o modelo)
- `sort_by`
- `order`

---

## 🚀 Endpoints

### 📁 Categorías

| Método | Endpoint | Descripción |
|-------|--------|------------|
| GET | /categories/ | Listar categorías |
| POST | /categories/ | Crear categoría |

---

### 🚜 Maquinaria

| Método | Endpoint | Descripción |
|-------|--------|------------|
| GET | /machinery/ | Listar maquinaria con filtros |
| POST | /machinery/ | Crear maquinaria |
| GET | /machinery/search | Búsqueda por texto |
| GET | /machinery/stats | Estadísticas |

---

## ▶️ Ejecución del Proyecto

### 1. Activar entorno virtual

### 2. Instalar dependencias


### 3. Ejecutar servidor


---

## 🌐 Documentación

Accede a Swagger UI:

👉 http://127.0.0.1:8000/docs

---




