# ---- Blockchain with Python, written by Paul Wiper ----
# ---- created following HackerNoon guide written by Daniel van Flymen ----

# Blockchain classes constructors create an empty list to store blockchain (BC) and another to store transactions
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        def new_block(self):
            # This creates a new block and then adds it to the chain
            pass

        def new_transaction(self):
            # Adds a new transaction to the list of transactions
            pass

        @staticmethod
        def hash(block):
            # Hashes a block
            pass
        
        @property
        def last_block(self):
            #returns last block in chain
            pass
