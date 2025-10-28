# Sistema de Gestión de Blog y Marketplace

### Descripción del Proyecto
Este proyecto académico implementa una plataforma web desarrollada con Django que combina funcionalidades de blog y marketplace. El sistema permite la gestión de contenido digital (blogs/artículos) con características de comercio electrónico, demostrando la aplicación práctica de conceptos avanzados de desarrollo web.


### Especificaciones Técnicas
#### Requisitos del Sistema
- Python 3.8+ (recomendado 3.10+)
- Django Framework
- Dependencias adicionales:
  - Pillow (procesamiento de imágenes)
  - mysqlclient/psycopg2 (opcional, para MySQL/PostgreSQL)

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

### Funcionalidades Implementadas
1. **Gestión de Contenido**
   - Catálogo de blogs/artículos
   - Sistema de búsqueda por título
   - Carga de imágenes de portada

2. **Sistema de Usuarios**
   - Panel de administración personalizado
   - Autenticación de administradores
   - Gestión de vendedores

3. **Comercio Electrónico**
   - Carrito de compras (Frontend)
   - Registro de pedidos
   - Procesamiento de ventas

### Rutas Principales
- `/` - Página principal y catálogo
- `/login/` - Acceso administrativo
- `/ventas/` - Panel de control de ventas (admin)
- `/agregarBlogs/` - Gestión de contenido
- `/pedidos/` - Datos de pedidos de usuario(se crea la venta )

### Notas
-  mantener actualizadas las dependencias
- Verificar compatibilidad de versiones en requirements.txt

