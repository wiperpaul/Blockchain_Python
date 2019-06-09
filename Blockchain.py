""" 
---- Blockchain with Python, written by Paul Wiper ----
---- created following HackerNoon guide written by Daniel van Flymen ----
"""
#Blockchain classes constructors create an empty list to store blockchain (BC)
#and another to store transactions
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #Create the genisis (first) block
        self.new_block(previous_hash=1, proof=100)

        def new_block(self, proof, previous_hash=None):
            """
            Creates new Block in BC

            :param proof: <int> The proof given by the Proof of Work Alg
            :param previous hash: (optional) <str> hash of the prev block
            :return: <dict> New block
            """

            block = {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transactions': self.current_transactions,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
                }

            # Clear the current transaction list
            self.current_transactions = []

            self.chain.append(block)
            return block

        def new_transaction(self):
            """
            Adds a new transaction to the list of transactions
            
            :param sender: <str> Address of Sender
            :param recipiet: <str> Address of Recepient
            :param amount: <int> Amount
            :return: <int> The index of the Block that will hold the transaction
            """
           
            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
                })

            return self.last_block['index'] + 1
            # return index for the block this trans info will be appended to by
            # incrementing last blocks index

        @staticmethod
        def hash(block):
            """ Hashes a block using SHA-256
                :param block: <dict> Block
                :return: <str>
            """

            # Must make sure Dictionary is ordered or hashes will be inconsistent
            block_string = json.dumps(block, sort_keys=True).encode()
            return hashlib.sha256(block_string).hexdigest()

            pass
        
        @property
        def last_block(self):
            #returns last block in chain
            pass
