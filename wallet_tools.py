from eth_account import Account
#from web3 import Web3
import csv
#import mnemonic
from multiprocessing import Pool, cpu_count
#import json


#生成钱包函数，24个助记词
def create_wallet(_):
    Account.enable_unaudited_hdwallet_features()
    account, mnemonic_phrase = Account.create_with_mnemonic(num_words=24)

    # 私钥
    private_Key = account.key.hex()

    # 地址
    address = account.address
    return {
        #"id": 0,
        "address": address,
        "mnemonic": mnemonic_phrase,
        "privateKey": private_Key
    }



#批量生成钱包函数
def createNewETHWallet(nums):
    wallets = []

    i = 0
    with Pool(processes=5) as pool:

        wallet = pool.map(create_wallet, range(nums))

        #print(wallet)
        wallets.append(wallet)
    return wallets

#保存生成的钱包为CSV文件
def saveETHWallet(jsonData):
    with open('wallets.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['address', 'mnemonic', 'privateKey'])

        csv_writer.writeheader()  #rows(['序号', '地址', '助记词', '私钥'])
        for row in jsonData:
            csv_writer.writerows(row)


if __name__ == "__main__":

    #print('seed phase:',generate_seed_phrase())
    nums = input('请输入创建钱包的数量: ')
    nums =int(nums)
    print("---- 开始创建钱包 ----")
    # 创建 nums 个随机钱包
    wallets = createNewETHWallet(nums)

    # 保存至 csv 文件
    saveETHWallet(wallets)
    print("---- 完成 ----")