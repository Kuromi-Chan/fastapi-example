from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOSTNAME")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")

DB_URL = f"mariadb+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

