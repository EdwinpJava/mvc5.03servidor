# mvdc5-servidor

## Configuracion

Configura estas variables de entorno antes de iniciar la aplicacion:

- `SECRET_KEY`: clave estable para firmar sesiones (obligatoria en produccion).
- `PASSWORD_REGISTRO_ESPECIAL`: clave para los registros especiales.
- `MAIL_USERNAME` y `MAIL_PASSWORD`: credenciales SMTP; el envio de correo se desactiva si faltan.
- `MAIL_DEFAULT_SENDER`: remitente opcional; si se omite, se usa `MAIL_USERNAME`.
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` y `DB_NAME`: conexion MariaDB/MySQL para `migrar_db.py`.

No subas archivos `.env`, bases de datos locales ni documentos de postulaciones.