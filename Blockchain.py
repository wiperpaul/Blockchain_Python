""" 
---- Blockchain with Python, written by Paul Wiper ----
---- created following HackerNoon guide written by Daniel van Flymen ----
"""
#Blockchain classes constructors create an empty list to store blockchain (BC) and another to store transactions

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        def new_block(self):
            pass

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
            # return index for the block this trans info will be appended to by incrementing last blocks index

        @staticmethod
        def hash(block):
            # Hashes a block
            pass
        
        @property
        def last_block(self):
            #returns last block in chain
            pass

        5UrJ0vaez5C1s