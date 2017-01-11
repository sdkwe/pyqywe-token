==========
pywe-token
==========

Wechat Access Token Module for Python.

Installation
============

::

    pip install pywe-token


Usage
=====

Token::

    # Sandbox: http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
    In [1]: from pywe_token import Token

    In [2]: token = Token('wx7aad305aed68bfe3', '9eac636765940ec286055c559ff84039')

    In [3]: token.
    token.API_DOMAIN           token.WECHAT_ACCESS_TOKEN  token.appid                token.get                  token.token
    token.OPEN_DOMAIN          token.access_token         token.expires_at           token.secret

    In [3]: token.access_token()
    Out[3]: u'ZhvSop2FJxAEyRLjyMIQfcfUS1tG76wGEz6hc-qgRFjaWqnLscdYBRBXVhH-SyiwXpeYTu-LfU2Fj4dTVVE3s-35MhVeaWbUMXmS3lPXgD4yrl8287yfmIXAseZI55_xUOQdADAEYA'


access_token::

    In [1]: from pywe_token import access_token

    In [2]: access_token('wx7aad305aed68bfe3', '9eac636765940ec286055c559ff84039')
    Out[2]: u'ysR7_hUtodKCF1nHjq8gFtagugB8oEOlK6hB6raMztveawVzpnqK2FtftbQGsczTj0h2kc1Gl8R7fjmGVPmXBp306WW8UZUteXqiOgxh3DL0usLRLQVRn56Oi-yigkSoSYNbAIAEKZ'


Redis Storage::

    In [1]: import redis_extensions as redis

    In [2]: r = redis.StrictRedisExtensions(host='localhost', port=6379, db=0)

    In [3]: from pywe_token import access_token

    In [4]: access_token('wx7aad305aed68bfe3', '9eac636765940ec286055c559ff84039', r)
    Out[4]: u'5kJwbClb1CBo-5Dz_a9hZi1GcqSnLkRV2aYFmjSBTGEvVrH81XhT2eUjunVSJn_ej2uFXLJarjC0dlI78r-HxCWtTNxSPC06ARG_QqE9FoP7VhJNFsPX5z7tsySsCyEgKEZbAIAGAV'

    In [5]: r.get('pywe:wechat:access:token')
    Out[5]: '5kJwbClb1CBo-5Dz_a9hZi1GcqSnLkRV2aYFmjSBTGEvVrH81XhT2eUjunVSJn_ej2uFXLJarjC0dlI78r-HxCWtTNxSPC06ARG_QqE9FoP7VhJNFsPX5z7tsySsCyEgKEZbAIAGAV'


Method
======

::

    class Token(WechatUtils):
        def __init__(self, appid=None, secret=None, redis_conn=None, redis_key=None):

    def access_token(self, appid=None, secret=None, redis_conn=None, redis_key=None):

