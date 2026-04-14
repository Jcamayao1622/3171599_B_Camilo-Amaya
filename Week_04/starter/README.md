# 🚜 Agrotech API - Gestión de Órdenes de Alquiler

API REST desarrollada con FastAPI para gestionar órdenes de alquiler de maquinaria agrícola, incluyendo manejo de estados, transiciones, respuestas estructuradas y manejo de errores.

---

## 🌱 Dominio

**Agrotech - Plataforma de Maquinaria Agrícola**

El sistema permite gestionar el ciclo de vida de una orden de alquiler de maquinaria, desde su solicitud hasta su finalización o cancelación.

---

## 🧱 Estructura del Proyecto

starter/
├── main.py
├── models.py
├── exceptions.py
├── schemas/
│ ├── request.py
│ └── response.py
├── routers/
│ └── rentals.py
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## 🚜 Entidad Principal

### RentalOrder

- id
- rental_code
- machinery_id
- client_name
- days
- total_price
- status
- requested_by
- notes
- created_at
- approved_at
- completed_at

---

## 🔄 Estados del Proceso

- `requested`
- `approved`
- `in_use`
- `completed`
- `cancelled`

---

## 🔁 Transiciones

| Estado Actual | Acción | Nuevo Estado |
|--------------|--------|-------------|
| requested | approve | approved |
| approved | start | in_use |
| in_use | complete | completed |
| requested / approved / in_use | cancel | cancelled |

---

## 🚀 Endpoints

### 📌 Órdenes de alquiler

| Método | Endpoint | Descripción |
|--------|---------|------------|
| POST | /rentals/ | Crear orden |
| GET | /rentals/{id} | Obtener orden |
| POST | /rentals/{id}/approve | Aprobar |
| POST | /rentals/{id}/start | Iniciar uso |
| POST | /rentals/{id}/complete | Completar |
| POST | /rentals/{id}/cancel | Cancelar |

---

## 📤 Response Models

### RentalResponse
- id
- rental_code
- status

### RentalDetailResponse
- Información completa sin datos sensibles internos

---

## ⚠️ Manejo de Errores

- `RentalNotFoundError` → 404
- `InvalidTransitionError` → 400

---

## ▶️ Ejecución

### 1. Activar entorno virtual


### 2. Instalar dependencias


### 3. Ejecutar servidor


---

## 🌐 Documentación

Swagger UI disponible en:

👉 http://127.0.0.1:8000/docs

---

## 🧪 Ejemplo de flujo

1. Crear orden (`requested`)
2. Aprobar (`approved`)
3. Iniciar uso (`in_use`)
4. Completar (`completed`)

---

## 🎯 Características

✔ API REST completa  
✔ Manejo de estados  
✔ Transiciones controladas  
✔ Manejo de errores  
✔ Response models limpios  
✔ Documentación automática (OpenAPI)  
