import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

access_key = '7wyBZ596dAYxmILIIZhWO5OBLlBKgzDQILUniZ1r'
secret_key = 'r7kUzsQ7Sq3FRgldvnX46WunPxj4jiP7rJRdP4sw'
server_url = 'https://api.upbit.com'

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', headers=headers)
print(res.json())