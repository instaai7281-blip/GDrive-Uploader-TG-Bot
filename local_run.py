import os
import builtins
import functools

# Force print to always flush immediately
builtins.print = functools.partial(builtins.print, flush=True)

# Set environment variables for GDrive-Uploader-TG-Bot
os.environ["PYTHONUNBUFFERED"] = "1"
os.environ["PORT"] = "8080"
os.environ["ENV"] = "true"
os.environ["API_HASH"] = "11b88c331c5d44fde57cf91de1a2156b"
os.environ["APP_ID"] = "27317669"
os.environ["BOT_TOKEN"] = "8053658721:AAE85g1ewKAqzs0QDWzhPO51dZlvW9sIn8A"
os.environ["DATABASE_URL"] = "sqlite:///gdrive_bot.db"
os.environ["ALT_PORT"] = "true"

if __name__ == "__main__":
    import bot
    print("[INFO] Starting bot with custom environment configuration...")
    bot.main()
