from curses import raw
import redis
import json

r = redis.StrictRedis(
    host='192.168.15.88',  # из Endpoint
    port=6379,  # из Endpoint
    password='P@ssw0rd!'  # ваш пароль
)

def get_data(query):
    data = r.get(query)
    if data != None: 
        data = json.loads(data)
    return data

def set_data(query,data):
    data = r.set(query,json.dumps(data))
    return True
