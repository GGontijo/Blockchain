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
        __sync = self.chain_sync()
        if not __sync:
            self.genesis_block()
        else: 
            self.blockchain = __sync
            print(self.blockchain)
        self.check_integrity()
        #self.block.new_block(self.blockchain, self.sync_data)
        
    def chain_sync(self) -> dict:
        self.__id_history = []
        self.sync_data = {}
        with open('blockchain.json', 'r') as f:
            __blockchain = json.load(f)
        if not __blockchain:
            print('Blockchain empty! Genesis block will be mined')
            return
        for block in __blockchain:
            __block_id = block['header']['id']
            print(f'Syncing block: {__block_id}')
            self.__id_history.append(__block_id)
        self.__last_id = self.__id_history[-1]
        print(f'Last block mined: {self.__last_id}')
        self.sync_data['id_history'] = self.__id_history
        self.sync_data['last_id'] = self.__last_id
        return __blockchain

    def genesis_block(self):
        self.blockchain = []
        new_block = self.block.new_block(self.blockchain, self.sync_data)
        self.blockchain.append(new_block)
        print('Genesis block created!')
        with open(self.LOCALCHAIN, 'w') as blockchainfile:
            json.dump(self.blockchain, blockchainfile, indent=4)
        return

        #with open(self.LOCALCHAIN, 'w') as blockchainfile:
        #    json.dump(self.blockchain, blockchainfile, indent=4)
        #    print(self.blockchain)

    def check_integrity(self) -> bool:
        __blockchain_height = len(self.blockchain)
        if __blockchain_height < 2:
            print('ok')
            return True
        __index = 1
        n_index = 0
        while __index <= (__blockchain_height - 1):
            n_hash = str(self.blockchain[__index]['header']['n_hash'])
            if n_hash != str(Cripto.hash(self.blockchain[n_index]['header']['n_hash'])):
                return False #previous block's hash changed!
            elif n_hash.startswith('000'):
                return False #hash invalid


    def difficult(self):
        pass

    def PoW(hash: str) -> int:
        pass

Blockchain = Blockchain()