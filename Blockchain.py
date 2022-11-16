import time
from Block import Block
import Cripto
import json
import configparser

class Blockchain:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.sections()
        CONFIG_FILE = 'blockchain.config'
        config.read(CONFIG_FILE)
        self.LOCALCHAIN = config['DEFAULT']['LOCALCHAIN']
        self.block = Block()
        blockchain_sync_data = self.init_chain_sync()
        if not blockchain_sync_data:
            self.genesis_block()
        else: 
            self.blockchain = blockchain_sync_data
        #if not self.check_chain_integrity():
        #    return
        #else:
        #    print('Blockchain integrity verified!')
        while True:
            self.mine()
            if not self.chain_sync():
                return
            #if not self.check_chain_integrity():
            #    return
            time.sleep(0)


    def mine(self):
        new_block = self.block.new_block(self.blockchain, self.sync_data)
        self.blockchain.append(new_block)
        with open(self.LOCALCHAIN, 'w') as blockchainfile:
            json.dump(self.blockchain, blockchainfile, indent=4)
        print(self.blockchain)
        
    def init_chain_sync(self) -> dict:
        self.__id_history = []
        self.__last_id = None
        self.__nonce_history = []
        self.sync_data = {}
        with open('blockchain.json', 'r') as f:
            __blockchain = json.load(f)
        if not __blockchain:
            print('Blockchain empty! Genesis block will be mined')
            return
        for block in __blockchain:
            __block_id = block['header']['id']
            __nonce_history = block['header']['nonce']
            print(f'Syncing block: {__block_id}')
            self.__id_history.append(__block_id)
            self.__nonce_history.append(__nonce_history)
        self.__last_id = self.__id_history[-1]
        print(f'Last block mined: {self.__last_id}')
        self.sync_data['id_history'] = self.__id_history
        self.sync_data['last_id'] = self.__last_id
        self.sync_data['nonce_history'] = self.__nonce_history
        return __blockchain

    def chain_sync(self):
        if not self.sync_data:
            print('Sync data not initialized!')
            return False

        with open('blockchain.json', 'r') as f:
            __blockchain = json.load(f)

        for block in __blockchain:
            __block_id = block['header']['id']
            __nonce_history = block['header']['nonce']
            print(f'Syncing block: {__block_id}')
            self.__id_history.append(__block_id)
            self.__nonce_history.append(__nonce_history)
        self.__last_id = self.__id_history[-1]
        print(f'Last block mined: {self.__last_id}')
        self.sync_data['id_history'] = self.__id_history
        self.sync_data['last_id'] = self.__last_id
        self.sync_data['nonce_history'] = self.__nonce_history
        return True


    def genesis_block(self):
        self.blockchain = []
        new_block = self.block.new_block(self.blockchain, self.sync_data)
        self.blockchain.append(new_block)
        print('Genesis block created!')
        with open(self.LOCALCHAIN, 'w') as blockchainfile:
            json.dump(self.blockchain, blockchainfile, indent=4)
        return

    def check_chain_integrity(self) -> bool:
        __blockchain_height = len(self.blockchain)
        if __blockchain_height < 2: 
            return True
        __index = 1
        n_index = 0
        while __index <= (__blockchain_height - 1):
            n_hash = self.blockchain[__index]['header']['n_hash']
            block_id = self.blockchain[__index]['header']['id']
            n_block_id = self.blockchain[n_index]['header']['id']
            if n_hash != Cripto.hash(self.blockchain[n_index]):
                print(f"Block hash {n_block_id} is invalid!")
                return False #previous block's hash changed!
            __difficult_dict = Cripto.difficult(block_id)
            __difficult = __difficult_dict['difficult']
            if not n_hash.startswith(__difficult):
                print(f"Block's nonce {n_block_id} is invalid!")
                return False #hash invalid
            __index = __index + 1
            n_index = n_index + 1
            return True

Blockchain = Blockchain()

