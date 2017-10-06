# -*- coding: utf-8 -*-

import redis_extensions as redis
from pywe_storage import RedisStorage
from pywe_token import Token, access_token, final_access_token

from local_wecfg_example import WECHAT


class TestTokenCommands(object):

    def test_token_mem(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        token = Token(appid=appid, secret=appsecret)
        access_token1 = token.access_token()
        assert isinstance(access_token1, basestring)

        access_token2 = access_token(appid=appid, secret=appsecret)
        assert isinstance(access_token2, basestring)

        access_token3 = final_access_token(cls=token, appid=appid, secret=appsecret)
        assert isinstance(access_token3, basestring)

        assert access_token1 == access_token3 != access_token2

    def test_token_redis(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        r = redis.StrictRedisExtensions(host='localhost', port=6379, db=0)
        storage = RedisStorage(r)

        token = Token(appid=appid, secret=appsecret, storage=storage)
        access_token1 = token.access_token()
        assert isinstance(access_token1, basestring)

        access_token2 = access_token(appid=appid, secret=appsecret, storage=storage)
        assert isinstance(access_token2, basestring)

        access_token3 = final_access_token(cls=token, appid=appid, secret=appsecret, storage=storage)
        assert isinstance(access_token3, basestring)

        assert access_token1 == access_token3 == access_token2
