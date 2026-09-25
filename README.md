# Pre-Entrega: Automatización de Pruebas QA

Proyecto de automatización de pruebas end-to-end sobre la plataforma web **SauceDemo** ([https://www.saucedemo.com](https://www.saucedemo.com)), desarrollado como parte del curso de Automatización QA.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje de Programación:** Python 3.14
- **Framework de Pruebas:** Pytest
- **Herramienta de Automatización Web:** Selenium WebDriver
- **Generación de Reportes:** Pytest-HTML
- **Control de Versiones:** Git / GitHub

---

## 📁 Estructura del Proyecto

```text
pre-entrega-automation-testing-[tu-nombre]/
├── utils/
│   ├── __init__.py
│   └── helpers.py            # Fixtures de Pytest y funciones de espera explícita
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py     # Casos de prueba automatizados (Login, Catálogo, Carrito)
├── reports/
│   └── reporte.html          # Reporte ejecutable generado en HTML
├── requirements.txt          # Lista de dependencias del proyecto
└── README.md                 # Documentación del proyecto