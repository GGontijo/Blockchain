import json

with open('blockchain.json', 'r') as f:
    blockchain = json.load(f)
    print(blockchain)