import hashlib
  

def hash(block: dict) -> str:
    __hash_data = str(block)
    __hash = hashlib.sha256(__hash_data.encode('utf-8')).hexdigest()
    return __hash

def PoW(block, __sync_data):
    if __sync_data:
        __nonce_history = __sync_data['nonce_history']
    else:
        __nonce_history = []
    nonce = 0
    PoW = False
    while PoW == False:
        difficult_helper = difficult(block['header']['id'])
        block_difficult = difficult_helper['difficult']
        block['header']['nonce'] = nonce
        print(f'Mining nonce: {nonce}')
        try_hash = str(hash(block))
        if not try_hash.startswith(block_difficult):
            nonce = nonce + 1
            continue
        elif nonce in __nonce_history:
            nonce = nonce + 1
            continue
        else:
            print(f'Block mined with nonce: {nonce}')
            print(f'Hash: {try_hash}')
            PoW = True
        return nonce

def difficult(block_id):
        '''Difficult increases every 2,016 blocks, 
        starting from 1 to n I'll be using just 64..'''
        epoch = int((int(block_id,16)) / 64) 
        difficult = '0' * (epoch + 1)
        return {'difficult': difficult, 'epoch': epoch}