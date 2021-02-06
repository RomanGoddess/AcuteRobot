import os, sys, logging
from functools import wraps
from telegram.ext import Updater, Defaults
from telegram import ChatAction, ParseMode
from acutebot.config import Config

TOKEN = Config.TOKEN
WORKERS = Config.WORKERS
TMDBAPI = Config.TMDBAPI
DB_URI = Config.DB_URI
GENIUS = Config.GENIUS
SPT_CLIENT_SECRET = Config.SPT_CLIENT_SECRET
SPT_CLIENT_ID = Config.SPT_CLIENT_ID
DEBUG = Config.DEBUG
ARLTOKEN = Config.ARL
APP_URL = Config.APP_URL
APIID = Config.APIID
APIHASH = Config.APIHASH
