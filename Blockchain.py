from Helpers import Helpers


blockchain = []
block = {}
header = {}
#'id' = some random hex increment
#'previous_hash' = blockchain[n-1]['header']['hash']
#'hash' = 'SOMETHING'
data = {}


class Blockchain:
    
    def __init__(self):
        self.blockchain = []
        self.block = {}
        self.header = {}
        self.data = {}
        self.id_history = ['0x1']
        self.helpers = Helpers()

    def populate_block(self, data: dict):
        __id_helper = self.helpers.id(self.id_history)
        self.header['id'] = __id_helper['new_id']
        self.header['hash'] = self.helpers.hash(self.block)
        self.header['n_hash'] = None
        self.data[''] = None
        self.block['header'] = self.header
        self.block['data'] = self.data
        print(self.block)

a = Blockchain()
dict = {}
a.populate_block(dict)



