import hashlib
import json
import time
import os
import requests
import sys
import random
import string
import threading
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = Block(
            data=self.current_transactions,
            previous_hash=previous_hash or self.hash(self.chain[-1])
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    def hash(self, block):
        sha = hashlib.sha256()
        sha.update(str(block.data).encode('utf-8'))
        sha.update(str(block.previous_hash).encode('utf-8'))
        return sha.hexdigest()

