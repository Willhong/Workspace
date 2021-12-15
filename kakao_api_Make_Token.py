import requests
from requests.api import request
import key
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = key.rest_api_key
redirect_uri = 'https://example.com/oauth'
uuu='https://kauth.kakao.com/oauth/authorize?client_id='+rest_api_key+'&redirect_uri='+redirect_uri+'&response_type=code'
uuu_friend='https://kauth.kakao.com/oauth/authorize?client_id='+rest_api_key+'&redirect_uri='+redirect_uri+'&response_type=code&scope=talk_message,friends'
print(uuu)

#authorize_code : 할때마다 불러오기
authorize_code = '5CDgVDmyOZvTClKYB4KGLyVmHinQypC5Taq-heL6JsuiCzCzuommE13D7Pcigh-Zef-3jwo9dRsAAAF9uRoOWg'


data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
# 1.
with open(r"./kakao_code.json","w") as fp:
    json.dump(tokens, fp)

#2.
with open("kakao_code.json","r") as fp:
    ts = json.load(fp)
print(ts)
print(ts["access_token"])