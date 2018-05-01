# -*- coding: utf-8 -*-

import time

from pywe_exception import WeChatException

from .basetoken import BaseToken


class Token(BaseToken):
    def __init__(self, appid=None, secret=None, storage=None, token_fetched_func=None):
        super(Token, self).__init__(appid=appid, secret=secret, storage=storage, token_fetched_func=token_fetched_func)
        # 获取access token, Refer: https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140183
        self.WECHAT_ACCESS_TOKEN = self.API_DOMAIN + '/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'

    def __about_to_expires(self, expires_at):
        return expires_at and expires_at - int(time.time()) < 60

    def __fetch_access_token(self, appid=None, secret=None, storage=None, token_fetched_func=None):
        # Update Params
        self.update_params(appid=appid, secret=secret, storage=storage, token_fetched_func=token_fetched_func)
        # Access Info Request
        access_info = self.get(self.WECHAT_ACCESS_TOKEN, appid=self.appid, secret=self.secret)
        # Request Error
        if 'expires_in' not in access_info:
            raise WeChatException(access_info)
        # Set Access Info into Storage
        expires_in = access_info.get('expires_in')
        access_info['expires_at'] = int(time.time()) + expires_in
        self.storage.set(self.access_info_key, access_info, expires_in)
        # If token_fetched_func, Call it with `appid`, `secret`, `access_info`
        if token_fetched_func:
            token_fetched_func(self.appid, self.secret, access_info)
        # Return Access Token
        return access_info.get('access_token')

    def access_token(self, appid=None, secret=None, storage=None, token_fetched_func=None):
        # Update Params
        self.update_params(appid=appid, secret=secret, storage=storage, token_fetched_func=token_fetched_func)
        # Fetch access_info
        access_info = self.storage.get(self.access_info_key)
        if access_info:
            access_token = access_info.get('access_token')
            if access_token and not self.__about_to_expires(access_info.get('expires_at')):
                return access_token
        return self.__fetch_access_token(self.appid, self.secret, self.storage, token_fetched_func=self.token_fetched_func)

    def refresh_access_token(self, appid=None, secret=None, storage=None, token_fetched_func=None):
        return self.__fetch_access_token(appid, secret, storage, token_fetched_func=token_fetched_func)

    def final_access_token(self, cls=None, appid=None, secret=None, token=None, storage=None, token_fetched_func=None):
        return token or self.access_token(appid or cls.appid, secret or cls.secret, storage=storage or cls.storage, token_fetched_func=token_fetched_func or cls.token_fetched_func)


token = Token()
access_token = token.access_token
refresh_access_token = token.refresh_access_token
final_access_token = token.final_access_token
