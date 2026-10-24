
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'server'))

from waitress import serve
from app import app

print("\n" + "="*60)
print("SERVIDOR DE MOVILIDAD DEL CONOCIMIENTO ACTIVO")
print("="*60)
print("IP LOCAL: 127.0.0.1")
print("ACCESO LOCAL: http://127.0.0.1:5000")
print("="*60 + "\n")

os.chdir(os.path.join(os.path.dirname(__file__), 'server'))

serve(
    app,
    host="0.0.0.0",
    port=5000,
    threads=12,
    connection_limit=1000,
    channel_timeout=120,
    url_prefix="",
    ident="Movilidad-Conocimiento-Server"
)

