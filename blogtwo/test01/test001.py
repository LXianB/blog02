# !/user/bin/env python
# -*- coding:utf-8 -*-

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

serializer = Serializer('secretkey', 3600)   # 两个参数分别是: 加密秘钥，加密过期时间3600秒
info = {'confirm':1}
res = serializer.dumps(info)   # 加密
print(res)
ress = serializer.loads(res)  # 解密
print(ress)