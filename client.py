#!/usr/bin/python3
import random
import string
import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

''' Client Class '''


class Client:
    """Creates Public and Private Keys"""
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify
        (self._public_key.exportKey(format='DER')).decode('ascii')


''' Testing '''

Taylor = Client()
print(Taylor.identity)
