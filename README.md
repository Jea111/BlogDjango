# Sistema de Gestión de Blog y tienda

### Descripción del Proyecto
Este proyecto académico implementa una plataforma web desarrollada con Django que combina funcionalidades de blog y tienda. El sistema permite la gestión de contenido digital (blogs/artículos) con características de comercio electrónico, sistema de reseñas y carrito de compras.

### Estado Actual del Proyecto
1. **Interfaz de Usuario**
   - Diseño responsive y limpio
   - Carousel funcional en página principal
   - Navegación 
   - Integración de Bootstrap para UI consistente

2. **Funcionalidades Core**
   - Sistema de carrito funcional con cálculos 
   - Gestión de blogs con imágenes
   - Sistema de reseñas por producto
   - Panel administrativo personalizado(admin/vendedor)

3. **Seguridad**
   - Protección CSRF implementada
   - Manejo básico de errores
   - Validación de formularios



### Especificaciones Técnicas
#### Requisitos del Sistema
- Python 3.10+
- Django Framework
- Dependencias adicionales:
  - Pillow (procesamiento de imágenes)
  - mysqlclient/para MySQL

1) Crear y activar entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Instalar dependencias

```powershell
pip install -r .\requirements.txt
```

3) Configurar la base de datos
 


4) Migraciones y superusuario

```powershell
python manage.py migrate
python manage.py createsuperuser
```

5) Ejecutar servidor de desarrollo

```powershell
python manage.py runserver
```

### Funcionalidades 
1. **Gestión de Contenido**
   - Catálogo de blogs/artículos
   - Sistema de búsqueda por título
   - Carga de imágenes de portada

2. **Sistema de Usuarios**
   - Panel de administración 
   - Autenticación de administradores
   - Gestión de vendedores

3. **Comercio Electrónico**
   - Carrito de compras 
   - Registro de pedidos
   - Procesamiento de ventas

### Rutas Principales
- `/` - Página principal y catálogo
- `/login/` - Acceso administrativo
- `/ventas/` - Panel de control de ventas (admin)
- `/agregarBlogs/` - Gestión de vende con nosotros
- `/pedidos/` - Datos de pedidos de usuario(se crea la venta )
- `/blog_comentado/<int:id>//` - Datos de reseñas por blog y se crea la reseña

### A tener en cuenta
- Verificar compatibilidad de versiones en requirements.txt
- Revisar periódicamente actualizaciones de seguridad
- Considerar implementar pruebas automatizadas
- Documentar cambios significativos en el código

