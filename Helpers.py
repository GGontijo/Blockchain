from datetime import datetime


def log_time() -> str:
    '''Função que retorna o DateTime atual em:
    >>> DD:MM:YY HH:MM:SS'''
    timeaux = datetime.now()
    return timeaux.strftime("%d/%m/%Y %H:%M:%S")
    
def new_id(__sync_data) -> str:
    if not __sync_data:
        return {'new_id': hex(0x1), 'last_id': None}
    else:
        __last_id = int(__sync_data['last_id'], 16)
        __new_id = hex(__last_id + 1)
        return {'new_id': __new_id, 'last_id': hex(__last_id)}