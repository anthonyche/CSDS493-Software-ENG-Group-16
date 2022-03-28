#@author Tiantian Pu

# -*- coding: utf-8 -*-
import pandas as pd 
import os
from src.getSourceCode import getSourceCode 
from src.getByteCode import getByteCode

#All directory paths of this file
base_dir = os.path.dirname(os.path.realpath('__file__'))
# The directory where the obtained contract source code is saved
sources_dir = f"{base_dir}/data/sourcecodes/"

# requests 
proxies={
    'http':'socks5://127.0.0.1:10808',
    'https':'socks5://127.0.0.1:10808'
}

# etherscan ApiKey, The free api is limited to five requests per second.
ApiKey = "2FCA2VENCVW1E1SGGS4N3N5CGGR3HKS6NT"
# Node rpc required by web3
provider = "https://api.edennetwork.io/v1/rpc"

# The list of verified contracts on the chain can be obtained directly from the etherscan api documentation
verified_contracts = pd.read_csv(f'{base_dir}/data/contract_address/export-verified-contractaddress-opensource-license.csv',  header=1, encoding="utf-8-sig").drop(0)

# print(verified_contracts.columns.to_list())

data_frame = pd.DataFrame(verified_contracts)

contracts_addr_list = data_frame['ContractAddress']

for i in range(1,10):
    
    # get source code
    source_code = getSourceCode(contract_address=contracts_addr_list[i], ApiKey=ApiKey, proxies=proxies)
    ''' get byte code'''
    
    # byte_code = getByteCode(provider=provider)
    
    # save source to local
    file_dir = f'{sources_dir}/{contracts_addr_list[i]}.sol'
    if not os.path.exists(file_dir):        
        with open(file_dir, 'w', encoding='utf-8') as f:
            f.write(source_code)
