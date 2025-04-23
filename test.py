import requests, json
import os

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
    token_pairs = response.json()

    for token_pair in token_pairs:
        chain = token_pair["chainId"]
        name = token_pair["baseToken"]["name"]
        symbol = token_pair["baseToken"]["symbol"]
        priceNative = token_pair["priceNative"]
        priceUsd = token_pair["priceUsd"]
        volume = token_pair["volume"]["h24"]
        token_data.append({
            "chain" : chain,
            "symbol" : symbol,
            "name" : name,
            "priceNative" : priceNative,
            "priceUsd" : priceUsd,
            "volume" : volume
        })
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(token_data, file, indent=4)
