# -*- coding: utf-8 -*-

import time

from pywe_exception import WeChatException
from pywe_utils import WechatUtils


class Token(WechatUtils):
    def __init__(self, appid=None, secret=None):
        # 获取access token, Refer: https://mp.weixin.qq.com/wiki/14/9f9c82c1af308e3b14ba9b973f99a8ba.html
        super(Token, self).__init__()
        self.WECHAT_ACCESS_TOKEN = self.API_DOMAIN + '/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
        self.appid = appid
        self.secret = secret
        self.token = None
        self.expires_at = None

    def __fetch_access_token(self, appid=None, secret=None):
        result = self.get(self.WECHAT_ACCESS_TOKEN, appid=appid or self.appid, secret=secret or self.secret)
        if 'expires_in' not in result:
            raise WeChatException(result)
        self.token = result.get('access_token')
        self.expires_at = int(time.time()) + result.get('expires_in')
        return self.token

    def access_token(self, appid=None, secret=None):
        if self.token and self.expires_at and self.expires_at - int(time.time()) > 60:
            return self.token
        return self.__fetch_access_token(appid, secret)


token = Token()
access_token = token.access_token