from datetime import datetime
import hashlib
import json

class Helpers:
    def log_time(self) -> str:
        '''Função que retorna o DateTime atual em:
        >>> DD:MM:YY HH:MM:SS'''
        aux = datetime.now()
        return aux.strftime("%d/%m/%Y %H:%M:%S")
        
    def hash(self, block: dict) -> str:
        __hash_data = ''
        for i in block:
            __hash_data = __hash_data + i 
        __hash = hashlib.sha256(__hash_data.encode('utf-8')).hexdigest()
        return __hash

    def new_id(self) -> str:
        __id_history = []
        with open('blockchain.json', 'r') as f:
            blockchain = f.readlines()
        if len(blockchain) == 0:
            print('ok')
            return {'new_id': hex(0x1), 'last_id': None}
        else:
            with open('blockchain.json', 'r') as f:
                blockchain = json.load(f)
            for block in blockchain:
                print(str(block['header']['id']))
                print(__id_history)
        __id_history = __id_history.sort()
        __last_id = int(__id_history[-1], 16)
        __new_id = hex(__last_id + 1)
        return {'new_id': __new_id, 'last_id': hex(__last_id)}

    def check_integrity(self) -> bool:
        pass

    def PoW(self, hash: str) -> int:
        pass