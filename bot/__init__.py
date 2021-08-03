#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & sunaif_adkar

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Created https://t.me/sunaif_adkar
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL")

MT_CHANNEL_USERNAME = os.environ.get("JOIN_MAIN_CHANNEL")

MASSAGE_PHOTO = os.environ.get("TEXT_MEG_PH")

MRK_YT_MASTER = os.environ.get("BOT_MASTER")

MT_GROUP = os.environ.get("G_ID_START")

MT_CHANNEL = os.environ.get("C_ID_START")

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
