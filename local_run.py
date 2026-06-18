import os

# Set environment variables for GDrive-Uploader-TG-Bot
os.environ["PORT"] = "8080"
os.environ["ENV"] = "true"
os.environ["API_HASH"] = "11b88c331c5d44fde57cf91de1a2156b"
os.environ["APP_ID"] = "27317669"
os.environ["BOT_TOKEN"] = "8146920201:AAHlctyHnhgLPQbqAon7gwoCLSnlDVC0cpc"
os.environ["DATABASE_URL"] = "sqlite:///gdrive_bot.db"

# Proxy configuration from user
os.environ["PROXY_HOSTNAME"] = "206.123.156.223"
os.environ["PROXY_PORT"] = "4074"
os.environ["PROXY_SCHEME"] = "socks5"

if __name__ == "__main__":
    import bot
    print("[INFO] Starting bot with custom environment configuration...")
    bot.main()
