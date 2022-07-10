import hashlib   

def hash(block: dict) -> str:
    __hash_data = ''
    for i in block:
        __hash_data = __hash_data + i 
    __hash = hashlib.sha256(__hash_data.encode('utf-8')).hexdigest()
    return __hash