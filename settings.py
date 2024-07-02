import os

from dotenv import load_dotenv

NAME = "IT Solutions parse"
HOST = "0.0.0.0"
PORT = 8000

load_dotenv()

HOST_URL = "https://www.farpost.ru"
HOMEPAGE_URL = HOST_URL + "/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Cookie": "ring=dbb792a0211ff848e5c1c4021858cf25; ring_session=1.3.1719830967.1719877280.1719881911.eXQwF4R81tP"
    "%2BigoknZmMqMXyUO8GJ9Wl0JncBsngJtk%3D; _ga=GA1.2.1122597280.1719830968; "
    "_gid=GA1.2.1856611485.1719830968; _ga_G0RWKN84TQ=GS1.1.1719877290.3.1.1719881910.60.0.0; "
    "_ga_64RVG4FR1N=GS1.2.1719877290.3.0.1719881911.0.0.0; services_far_east_counter=13",
    "Host": "www.farpost.ru",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
}

DB_DRIVER = "postgresql"
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

ALGORITHM = os.environ.get("ALGORITHM")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEFAULT_COOKIE_SETTINGS = {"httponly": True}

ALLOW_ORIGIN = "http://localhost"

DB_FULL_URL = f"{DB_DRIVER}+asyncpg://{DB_USER}:{DB_PASS}@{DB_URL}/{DB_NAME}"
