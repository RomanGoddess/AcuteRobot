import os, sys, logging
from functools import wraps
from telegram.ext import Updater, Defaults
from telegram import ChatAction, ParseMode
from acutebot.config import Config

TOKEN = os.environ.get("TOKEN")
WORKERS = int(os.environ.get("WORKERS", 8))
TMDBAPI = os.environ.get("TMDBAPI")
DB_URI = os.environ.get("DATABASE_URL")
GENIUS = os.environ.get("GENIUS")
SPT_CLIENT_SECRET = os.environ.get("SPT_CLIENT_SECRET")
SPT_CLIENT_ID = os.environ.get("SPT_CLIENT_ID")
DEBUG = bool(os.environ.get("DEBUG", False))
ARLTOKEN = os.environ.get("ARL")
APP_URL = os.environ.get("APP_URL")
APIID = os.environ.get("APIID")
APIHASH = os.environ.get("APIHASH")
