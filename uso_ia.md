# Registro de Uso de Inteligencia Artificial (uso_ia.md)

## Parte 1: Registro de Consultas y Prompts

1. **Poblamiento inicial de la base de datos**
   - **Prompt:** *"Genera una fixture JSON de Django para el modelo catalogo.Producto con 40 productos de ferretería chilenos realistas con nombre, categoría, precio y stock."*
   - **Uso:** Copié el formato JSON generado, ajusté los nombres de los campos para que coincidieran con mi modelo y lo cargué usando `python manage.py loaddata productos.json`.

2. **Lógica del carrito de compras y usuarios**
   - **Prompt:** *"¿Cómo implemento un carrito de compras básico en Django con autenticación y descuento de stock al confirmar?"*
   - **Uso:** Utilicé la estructura sugerida para crear los modelos y las vistas del carrito, adaptando los decoradores de seguridad para el administrador y los clientes.

---

## Parte 2: Explicación del Proceso

Usé la inteligencia artificial principalmente para que me ayudara a generar los datos de prueba de la ferretería y para estructurar la lógica del carrito de compras y los formularios de Django, ya que me ahorró bastante tiempo en la escritura repetitiva de código. La mayoría de las respuestas sobre los modelos y las vistas me sirvieron harto tal cual, pero tuve que corregir manualmente algunos detalles en las plantillas HTML, especialmente los enlaces de las rutas y los botones de administración para que no me arrojaran errores de nombres. En todo este proceso aprendí cómo interactúan las vistas con el ORM de Django y la importancia de validar bien el stock antes de descontar los productos.