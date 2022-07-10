from datetime import datetime
import json

def log_time() -> str:
    '''Função que retorna o DateTime atual em:
    >>> DD:MM:YY HH:MM:SS'''
    timeaux = datetime.now()
    return timeaux.strftime("%d/%m/%Y %H:%M:%S")
    
def new_id() -> str:
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
            __id_history.append(block['header']['id'])
    __last_id = int(__id_history[-1], 16)
    __new_id = hex(__last_id + 1)
    return {'new_id': __new_id, 'last_id': hex(__last_id)}