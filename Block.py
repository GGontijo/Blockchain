from Helpers import Helpers
import json

class Block:
    
    def __init__(self):
        self.block = {}
        self.header = {}
        self.data = {}
        self.helpers = Helpers()

    def new_block(self, data: dict):
        __id_helper = self.helpers.new_id()
        self.header['id'] = __id_helper['new_id']
        self.header['hash'] = self.helpers.hash(self.block)
        self.header['n_hash'] = None
        self.header['timestamp'] = self.helpers.log_time()
        #self.header['nonce'] = self.helpers.PoW()
        self.data[''] = None
        self.block['header'] = self.header
        self.block['data'] = self.data
        with open('blockchain.json', 'w') as blockchainfile:
            json.dump(self.block, blockchainfile, indent=4)
        return self.block
    

    def chain_sync(self):
        pass

a = Block()
dict = {}
print(a.new_block(dict))



