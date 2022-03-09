import hashlib
import json
import time
import os
import requests
import sys
import random
import string
import threading

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return str(self.data)