import os
import sys
import socket
import platform

class ServerManager:
    def __init__(self, host="0.0.0.0", port=5000):
        self.host = host
        self.port = port
        self.app_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "server")
        sys.path.insert(0, self.app_path)

    def get_local_ip(self):
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return local_ip
        except:
            return "127.0.0.1"

    def print_server_info(self):
        local_ip = self.get_local_ip()
        print("\n" + "=" * 60)
        print("SERVIDOR DE MOVILIDAD DEL CONOCIMIENTO ACTIVO")
        print("=" * 60)
        print(f"IP LOCAL: {local_ip}")
        print(f"ACCESO LOCAL: http://127.0.0.1:{self.port}")
        print(f"ACCESO RED: http://{local_ip}:{self.port}")
        print("=" * 60 + "\n")

    def start_windows(self):
        try:
            os.chdir(self.app_path)
            from waitress import serve
            from app import app

            self.print_server_info()
            serve(
                app,
                host=self.host,
                port=self.port,
                threads=12,
                connection_limit=1000,
                channel_timeout=120,
                url_prefix="",
                ident="Movilidad-Conocimiento-Server"
            )
        except ImportError as e:
            print(f"Error: Falta instalar dependencias. {e}")
            print("Por favor ejecuta: pip install -r server/requirements.txt")
        except Exception as e:
            print(f"Error al iniciar el servidor en Windows: {e}")

    def start_linux(self):
        try:
            os.chdir(self.app_path)
            import gunicorn.app.base
            from app import app

            class FlaskApplication(gunicorn.app.base.BaseApplication):
                def __init__(self, app, options=None):
                    self.options = options or {}
                    self.application = app
                    super().__init__()

                def load_config(self):
                    config = {key: value for key, value in self.options.items()
                            if key in self.cfg.settings and value is not None}
                    for key, value in config.items():
                        self.cfg.set(key.lower(), value)

                def load(self):
                    return self.application

            options = {
                'bind': f"{self.host}:{self.port}",
                'workers': 4,
                'threads': 4,
                'timeout': 120,
            }

            self.print_server_info()
            FlaskApplication(app, options).run()
        except ImportError as e:
            print(f"Error: Falta instalar dependencias. {e}")
            print("Por favor ejecuta: pip install -r server/requirements.txt")
        except Exception as e:
            print(f"Error al iniciar el servidor en Linux: {e}")

    def start(self):
        os_name = platform.system()
        if os_name == "Windows":
            self.start_windows()
        elif os_name == "Linux":
            self.start_linux()
        else:
            print(f"Sistema operativo {os_name} no compatible para inicio automático.")
            print("Por favor usa el servidor Flask de desarrollo:")
            print("  flask run --host=0.0.0.0 --port=5000")


if __name__ == "__main__":
    manager = ServerManager()
    manager.start()

