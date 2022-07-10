import json

class Block:
    
    def __init__(self):
        self.block = {}
        self.header = {}
        self.data = {}

    def new_block(self, data: dict):
        __id_helper = self.helpers.new_id()
        self.header['id'] = __id_helper['new_id']
        self.header['n_hash'] = None
        self.data['timestamp'] = self.helpers.log_time()
        #self.header['nonce'] = self.helpers.PoW()
        self.data[''] = None
        self.block['header'] = self.header
        self.block['data'] = self.data
        self.blockchain.append(self.block)
        with open('blockchain.json', 'w') as blockchainfile:
            json.dump(self.blockchain, blockchainfile, indent=4)
            print(self.blockchain)
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




