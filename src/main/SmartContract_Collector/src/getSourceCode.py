# -*- coding: utf-8 -*-
import requests
import json

def getSourceCode(contract_address, ApiKey, proxies):
    # etherscan api链接
    url_key = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={ApiKey}"
    
    result = ""
    
    if proxies:
        result = requests.get(url_key, proxies=proxies,verify=False)
    else:
        result = requests.get(url_key)
    source_code = ""
    try:
        source_code = json.loads(result.content.decode(encoding='utf-8'))['result'][0]['SourceCode']        
    except Exception as e:
        print(f"error: {e}")
    return source_code




