# demo
描述：获取eth链上已验证合约

## 目录说明
data 文件夹： 保存数据文件。此目录下的子文件夹： bytecodes 用于保存获取到的链上合约编译好的字节码， contract_address 用于保存从etherscan 下载的已经验证过的合约地址， sourcecodes 用于保存获取到的链上合约的源码

docs 文件夹: 用于保存相关文档、样式、图片等资源

src 文件夹: 用于保存python 文件

main.py： 主程序文件

## 程序说明
获取链上合约源码，主要用到的是etherscan 的api。
![](./docs/imgs/etherscan_api_get_verified_contract.jpg)
具体说明请参阅[官方说明](https://docs.etherscan.io/api-endpoints/contracts)

获取合约需要到etherscan 注册，获取免费请求ApiKey
登陆链接为[login](https://etherscan.io/login)

获取合约源码需要提前准备已经验证过的合约部署地址，官方下载链接为[open-source-contract-codes](https://etherscan.io/exportData?type=open-source-contract-codes)

获取已部署的二进制文件，可以使用web3.py, 官方开发文档链接为][web3.py](https://web3py.readthedocs.io/en/stable/web3.eth.html?highlight=eth_getCode#web3.eth.Eth.getCode)

## 运行说明

### 运行环境
运行环境为python 3.7.9

### 安装依赖库
```
pip install -r requirements.txt  
```

### 在main.py里设置好apikey， 运行主程序
```
python main.py
```

