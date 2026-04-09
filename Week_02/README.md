# 🚜 Agrotech API CRUD

## 📌 Descripción

API REST desarrollada con FastAPI y Pydantic para gestionar maquinaria agrícola.
Implementa operaciones CRUD completas con validación de datos.

---

## ⚙️ Funcionalidades

* ➕ Crear maquinaria
* 📋 Listar maquinaria (con paginación)
* 🔍 Obtener maquinaria por ID
* 🔎 Buscar por código único
* ✏️ Actualización parcial
* 🗑️ Eliminación

---

## 🧠 Validaciones

* Código único con formato `ABC-123`
* Ubicación con formato `A-01`
* Precio mayor a 0
* Potencia mayor o igual a 0

---

## 🛠️ Tecnologías

* FastAPI
* Pydantic v2
* Docker

---

## ▶️ Ejecución

```bash id="f8y1mv"
docker compose up --build
```

---

## 🌐 Acceso

http://localhost:8000/docs

---

## 📊 Dominio

Gestión de maquinaria agrícola (**Agrotech**)
