from gc import get_referents
from operator import ge
import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, json={"peoduct_id":123}) #HTTP REQUEST
# print(get_responce.text) #print raw text responce

# HTTP REQUEST  -->>  HTML
# REST API HTTP REQUEST   --->>  JSON (XML)

print(get_responce.json())