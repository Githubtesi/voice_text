import configparser
import os

FILE_NAME = "config.ini"
PAIRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(PAIRENT_DIR, FILE_NAME)

config = configparser.ConfigParser()
config.read(filenames=FILE_PATH, encoding="utf-8")

time = config["DEFAULT"]["wait_time"]