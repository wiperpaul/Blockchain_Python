""" 
---- Blockchain with Python, written by Paul Wiper ----
---- created following HackerNoon guide written by Daniel van Flymen ----
"""

import hashlib
import json

from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

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
        
        @property
        def last_block(self):
            #returns last block in chain
            pass

        def proof_of_work(self, last_proof):
            """
            Proof of work Alg
            - Find a number x such that hash(px) contains leading 4 zeros 
            - p being the previous proof and x being the new proof

            :param last_proof: <int>
            :return: <int>
            """
            proof = 0
            while self.valid_proof(last_proof, proof) is False:
                proof += 1

            return proof

        @staticmethod
        def valid_proof(last_proof, proof):
            """
            Validates the proof: Does hash(last_proof, proof) contain 4 leading zeros?

            :param last_proof: <int> Previous Proof
            :param proof: <int> Current Proof
            :return: <bool> True if correct, False if not.
            """

            guess = f'{last_proof}{proof}'.encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "0000"

        """

        ----CODE FOR FLASK AND NODE SETUP----
        
        """

        # Instantiate Node
        app = Flask(__name__)

        # Generate Unique id for node
        node_identifier = str(uuid4()).replace('-', '')

        # Instantiate the Blockchain ( STILL CONFUSED ABOUT THIS PART )
        blockchain = Blockchain()

        # Creates /mine endpoint which is a get request
        @app.route('/mine', methods=['GET'])
        def mine():
            return "Mine a new Block"

        # Creates the /transactions/new endpoint which is a POST req
        # well be sending data to this endpoint
        @app.route('/transactions/new', methods=['POST'])
        def new_transaction():
            values = request.get_json()

            # Check required fields are in the POST'ed data
            required = ['sender', 'recipient', 'amount']
            if not all(k in values for k in required):
                return 'Missing values', 400

            # Create a new transaction
            index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

            response = {'message': f'Transaction will be added to block {index}'}
            return jsonify(response), 201

        # Creates the chain endpoint which returns the full blockchain
        @app.route('/chain', methods=['GET'])
        def full_chain():
            response = {
                'chain': blockchain.chain,
                'length': len(blockchain.chain),
                }
            return jsonify(response), 200

        # Runs the server on port 5000
        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000)

        # Mining Endpoint
        @app.route('/mine', methods=['GET'])
        def mine():
            #run te proof of work alg to get the next proof
            last_block = blockchain.last_block
            last_proof = last_block['proof']
            proof = blockchain.proof_of_work(last_proof)

            # Reward for finding a proof
            # Sender = "0" signifies that node has mined a new coin
            blockchain.new_transaction(
                sender="0",
                recepient=node_identifier,
                amount=1,
            )

            #Forge new block by adding to chain
            previous_hash = blockchain.hash(last_block)
            block = blockchain.new_block(proof, previous_hash)

            response = {
                'message': "New Block Forged",
                'index': block['index'],
                'transactions': block['transactions'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                }
            return jsonify(response), 200

