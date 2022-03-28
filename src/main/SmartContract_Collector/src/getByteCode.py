from web3 import Web3

def getByteCode(provider, contract_addr):
    
    if 'http' in provider:
        w3 = Web3(Web3.HTTPProvider(provider))
    elif 'wss' in provider:
        w3 = Web3(Web3.WebsocketProvider(provider))
    else:
        w3 = Web3(Web3.HTTPProvider("https://api.edennetwork.io/v1/rpc"))
    byte_code = ""
    try:
        byte_code = w3.eth.get_code(contract_addr)
    except Exception as e:
        print(f"error in get byte code: {e}")
    return byte_code.hex()