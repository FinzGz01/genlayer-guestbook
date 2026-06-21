# { "Depends": "py-genlayer:test" }
from genlayer import *

class Storage(gl.Contract):
    def __init__(self, initial_storage: str):
        self.storage = initial_storage

    @gl.public.write
    def update_storage(self, new_storage: str):
        self.storage = new_storage

    @gl.public.read
    def get_storage(self):
        return self.storage
