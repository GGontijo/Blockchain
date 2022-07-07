import hashlib

class Helpers:
    def hash(self, block: dict) -> str:
        __hash_data = ''
        for i in block:
            __hash_data = __hash_data + i 
        __hash = hashlib.sha256(__hash_data.encode('utf-8')).hexdigest()
        return __hash

    def id(self, id_history: list) -> str:
        id_history.sort()
        __last_id = int(id_history[-1], 16)
        __new_id = hex(__last_id + 1)
        return {'new_id': __new_id, 'last_id': hex(__last_id)}


    def check_integrity(self) -> bool:
        pass
