FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=3000

WORKDIR /app

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ .

# Carpetas persistentes: base SQLite y archivos subidos (montar como volumes en Dokploy)
RUN mkdir -p instance static/uploads/postulaciones

EXPOSE 3000

# 1 worker: el hilo de recordatorios diarios corre por proceso (evita correos duplicados)
# y SQLite no tolera bien escrituras desde varios procesos. Los threads dan la concurrencia.
CMD gunicorn app:app --bind 0.0.0.0:${PORT} --workers 1 --threads 8 --timeout 120
