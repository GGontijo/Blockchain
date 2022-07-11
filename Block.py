import Helpers
import Cripto
import json

class Block:
    def __init__(self):
        self.block = {}
        self.header = {}
        self.data = {}

    def new_block(self, data, __sync_data):
        __id_helper = Helpers.new_id(__sync_data)
        self.header['id'] = __id_helper['new_id']
        self.data['timestamp'] = Helpers.log_time()
        self.data[''] = None

        if self.header['id'] == '0x1':
            self.header['n_hash'] = 'genesis_block'
            self.header['nonce'] = None
            self.block['header'] = self.header
            self.block['data'] = self.data
            return self.block
        else:
            n_index = (int(self.header['id'], 16) - 2)
            self.header['n_hash'] = Cripto.hash(data[n_index])
            self.header['nonce'] = None
            self.block['header'] = self.header
            self.block['data'] = self.data
            self.block['header']['nonce'] = Cripto.PoW(self.block, __sync_data)
            return self.block



'''
Block 1:
    header:
        id 
        previous hash
    data:
        transactions
----------------------------------------------
            Block 2:
                header:
                    id 
                    previous hash
                data:
                    transactions
--------------------------------------------
                        Block 3:
                            header:
                                id 
                                previous hash
                            data:
                                transactions
                                '''




