from Blockhelpers import Helpers
from Block import Block
import configparser

class Blockchain:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.sections()
        CONFIG_FILE = 'blockchain.config'
        config.read(CONFIG_FILE)
        self.localchain = config['DEFAULT']['LOCALCHAIN']
        self.helpers = Helpers()
        self.block = Block()
        self.blockchain = []
        self.chain_sync()

    def chain_sync(self):
        
        pass



    def check_integrity() -> bool:
        pass

    def PoW(hash: str) -> int:
        pass

Blockchain = Blockchain()