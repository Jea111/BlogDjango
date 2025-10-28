# BlogDjango

Proyecto Django sencillo que funciona como una pequeña tienda/marketplace de "blogs" (artículos/libros). Permite agregar productos con portada, mostrar catálogo, buscar por título y registrar pedidos/ventas de los usuarios.

Contenido
- `blog/` - app principal con modelos, vistas, URLs y plantillas.
- `blog_proyect/` - configuración del proyecto (settings, urls).
- `static/` - CSS y JS usados en las plantillas.
- `media/` - archivos subidos (portadas).

Requisitos
- Python 3.8+ (recomendado 3.10+)
- Dependencias listadas en `requeriments.txt` 

Contenido del archivo de dependencias :
- Django
- pillow
- mysqlclient (si usas MySQL)
- psycopg2 (si usas PostgreSQL)

Rápida guía de instalación (Windows - PowerShell)

1) Crear y activar entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Instalar dependencias

```powershell
pip install -r .\requeriments.txt
```

3) Configurar la base de datos

- El proyecto actualmente usa configuración MySQL en `blog_proyect/settings.py`.
- Para desarrollo rápido puedes usar sqlite3: reemplaza `DATABASES` en `blog_proyect/settings.py` por:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```


4) Migraciones y superusuario

```powershell
python manage.py migrate
python manage.py createsuperuser
```

5) Ejecutar servidor de desarrollo

```powershell
python manage.py runserver
```

Uso básico de la aplicación
- Página principal (`/`): lista de productos (blogs), búsqueda por título y carrito en frontend.
- login (login/) : login para administradores
- ventas (ventas/) panel de administracion solo para administradpres

- `agregarBlogs/`: formulario para subir un nuevo blog (título, portada, autor, precio).
- `pedidos/`: formulario para registrar un comprador y enviar el carrito (la vista espera un JSON en el campo `carrito`).

Notas importantes y recomendaciones

- Versiones: hay incompatibilidades entre la versión de Django en comentarios/migraciones y la versión en `requeriments.txt`. Alinea la versión deseada y actualiza `requeriments.txt` o regenera migraciones si cambias a una versión mayor.
