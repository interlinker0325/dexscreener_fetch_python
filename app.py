import requests
import os
import json

response = requests.get(
    "https://api.dexscreener.com/token-profiles/latest/v1",
    headers={"Accept":"*/*"},
)

data = response.json()
# print(data, "data")

token_data = []
for token in data:
    chainID = token["chainId"]
    tokenAddress = token["tokenAddress"]
    print(chainID, tokenAddress, "firstround===>")

    url = f"https://api.dexscreener.com/token-pairs/v1/{chainID}/{tokenAddress}"
  
    response = requests.get(url, headers={"Accept": "*/*"})
    token_pair = response.json()
    print(token_pair, "token_pair")
    token_data.extend(token_pair)
with open('token_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(token_data, json_file, indent=4)