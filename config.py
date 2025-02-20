#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7672004632:AAHohyBfssnv2Nlscz0tqiji3r1I7pfsdUc")
    API_ID = int(os.environ.get("API_ID", "23069582"))
    API_HASH = os.environ.get("API_HASH", "b3b56eaf67828684f54d540f684fdf1f")
    AUTH_USERS = "1780523256"

