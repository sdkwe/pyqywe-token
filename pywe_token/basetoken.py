# -*- coding: utf-8 -*-

from pywe_base import BaseWechat
from pywe_storage import MemoryStorage


class BaseToken(BaseWechat):
    def __init__(self, appid=None, secret=None, token=None, storage=None, expires_at=None):
        super(BaseToken, self).__init__()
        self.appid = appid
        self.secret = secret
        self.token = token
        self.storage = storage or MemoryStorage()
        self.expires_at = expires_at
