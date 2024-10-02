import requests
from urllib.parse import quote

my_key = 'test_fb54c8ad27d7dd07ceb73cd704ef73bf9b1fa33371c4344249fe6f3b93c7cb14efe8d04e6d233bd35cf2fabdeb93fb0d'

def fn_get_oguild_id(guild_name, world_name):
    url = (f"https://open.api.nexon.com/maplestory/v1/guild/id?guild_name={guild_name}&world_name={world_name}")
    headers = {'x-nxopen-api-key': my_key}
    res = requests.get(url, headers=headers)
    guild_name = quote(guild_name)
    world_name = quote(world_name)
    if res.status_code == 200:
        data = res.json()
        return data['oguild_id']
print(fn_get_oguild_id("고로케","크로아"))

def fn_get_guild_basic():
    url = (f"https://open.api.nexon.com/maplestory/v1/guild/basic?oguild_id=24415afb8c3b6f5e484f125810b0572c&date=KST%2C%202024-09-15")