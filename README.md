# Proyecto de Pre-Entrega - Automation Testing con Selenium y Pytest

Este proyecto contiene la suite de pruebas automatizadas de interfaz de usuario (UI) para la plataforma e-commerce [SauceDemo](https://www.saucedemo.com/), desarrollada como parte de la Pre-Entrega del curso de Automation Testing.

## Propósito del Proyecto
El objetivo es validar de forma automatizada los flujos principales de la aplicación SauceDemo, asegurando que las funcionalidades críticas operen correctamente:
- Autenticación y control de acceso.
- Visualización y navegación del catálogo de productos.
- Interacción con el carrito de compras (agregar productos y verificar contadores).

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Framework de Pruebas:** Pytest
- **Herramienta de Automatización Web:** Selenium WebDriver
- **Generación de Reportes:** pytest-html
- **Navegador:** Google Chrome

## Estructura del Proyecto

```text
pre-entrega-automation-testing-gabriel-malave/
├── reports/            # Archivos de reportes HTML generados
├── tests/              # Test cases automatizados
│   ├── test_login.py      # Pruebas de autenticación
│   ├── test_inventory.py  # Pruebas de catálogo y navegación
│   └── test_cart.py       # Pruebas del carrito de compras
├── utils/              # Funciones auxiliares y utilidades
├── conftest.py         # Configuración global del WebDriver (Fixtures de Pytest)
├── pytest.ini          # Configuración global de Pytest
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyec