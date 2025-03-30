#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7920777535:AAG1kQ8r1qxm01EMm5xi_qYIf5VlKrcr11U")
    API_ID = int(os.environ.get("API_ID", "23069582"))
    API_HASH = os.environ.get("API_HASH", "b3b56eaf67828684f54d540f684fdf1f")
    AUTH_USERS = "1780523256"

