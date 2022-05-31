from curses import raw
import redis
import json
import yaml

with open("./env.yaml") as file:
            evariables = yaml.safe_load(file)

r = redis.StrictRedis(
    host=evariables['redis']['ip'],  # из Endpoint
    port=evariables['redis']['port'],  # из Endpoint
    password=evariables['redis']['pass']  # ваш пароль
)

def get_data(query):
    data = r.get(query)
    if data != None: 
        data = json.loads(data)
    return data

def set_data(query,data):
    data = r.set(query,json.dumps(data))
    return True
