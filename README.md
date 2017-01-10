# pywe-token

Wechat Access Token Module for Python.

# Installation

```shell
pip install pywe-token
```

# Usage

* Token
  ```python
  # Sandbox: http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login
  In [1]: from pywe_token import Token

  In [2]: token = Token('wx7aad305aed68bfe3', '9eac636765940ec286055c559ff84039')

  In [3]: token.
  token.API_DOMAIN           token.WECHAT_ACCESS_TOKEN  token.appid                token.get                  token.token
  token.OPEN_DOMAIN          token.access_token         token.expires_at           token.secret               

  In [3]: token.access_token()
  Out[3]: u'ZhvSop2FJxAEyRLjyMIQfcfUS1tG76wGEz6hc-qgRFjaWqnLscdYBRBXVhH-SyiwXpeYTu-LfU2Fj4dTVVE3s-35MhVeaWbUMXmS3lPXgD4yrl8287yfmIXAseZI55_xUOQdADAEYA'
  ```

* access_token
  ```python
  In [1]: from pywe_token import access_token

  In [2]: access_token('wx7aad305aed68bfe3', '9eac636765940ec286055c559ff84039')
  Out[2]: u'ysR7_hUtodKCF1nHjq8gFtagugB8oEOlK6hB6raMztveawVzpnqK2FtftbQGsczTj0h2kc1Gl8R7fjmGVPmXBp306WW8UZUteXqiOgxh3DL0usLRLQVRn56Oi-yigkSoSYNbAIAEKZ'
  ```

# Method

```python
class Token(WechatUtils):
    def __init__(self, appid=None, secret=None):

def access_token(self, appid=None, secret=None):
```
