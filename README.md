# 🏟️ TuPrimeraPagina + Paganini

## 💻 Proyecto: Tienda de Camisetas Retro

Este proyecto fue desarrollado como parte del curso de Python de Coderhouse.  
Consiste en una aplicación web creada con Django, que simula una tienda online de camisetas de fútbol retro.

---

## ⚙️ Tecnologías utilizadas
- Python 3.13  
- Django 5.2.8  
- HTML, CSS  
- SQLite3  

---

## 🧩 Patrón MVT implementado

- **Modelos (Models):**  
  - `Camiseta` → representa las camisetas disponibles en la tienda.  
  - `Equipo` → agrupa las camisetas según el club.  
  - `Cliente` → contiene los datos de los clientes registrados.

- **Vistas (Views):**  
  - Listados, formularios y buscador integrados.  
  - Sistema de carrito de compras funcional.  

- **Templates (Templates):**  
  - Herencia de plantillas implementada en `base.html`  
  - Cada página hereda estructura y navegación comunes.

---

## 🧾 Funcionalidades
- Herencia de plantillas para todas las vistas.  
- Formulario para agregar **Camisetas**, **Equipos** y **Clientes**.  
- Búsqueda de camisetas en la base de datos.  
- Carrito de compras simple.  
- Acceso a panel de administración (`/admin`).

---

## 🔍 Cómo probar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/augustojpaganini/TuPrimeraPagina-Paganini.git
