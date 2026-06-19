import os
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from pyrogram import Client
from config import Config

# Plugins directory
plugins = dict(root="plugins")

class HealthCheckHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "ok", "bot": "running"}')

    def log_message(self, format, *args):
        # Silence standard HTTP logs to keep bot console clean
        pass

def start_health_check():
    port = int(os.environ.get("PORT", 8080))
    TCPServer.allow_reuse_address = True
    try:
        with TCPServer(("0.0.0.0", port), HealthCheckHandler) as httpd:
            print(f"[INFO] Health check server running on port {port}")
            httpd.serve_forever()
    except Exception as e:
        print(f"[ERROR] Health check server failed: {e}")

def main():
    # Start health check server in a background thread to satisfy Railway/Heroku port binding
    t = threading.Thread(target=start_health_check, daemon=True)
    t.start()

    proxy = None
    if Config.PROXY_HOSTNAME and Config.PROXY_PORT:
        proxy = dict(
            scheme=Config.PROXY_SCHEME,
            hostname=Config.PROXY_HOSTNAME,
            port=Config.PROXY_PORT
        )
        if Config.PROXY_USERNAME:
            proxy["username"] = Config.PROXY_USERNAME
        if Config.PROXY_PASSWORD:
            proxy["password"] = Config.PROXY_PASSWORD
    print(f"[DEBUG] Pyrogram Client initialized with proxy: {proxy}")

    try:
        app = Client(
            "GDrive-Uploader-TG-Bot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            plugins=plugins,
            proxy=proxy,
            alt_port=Config.ALT_PORT
        )
        app.run()
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
