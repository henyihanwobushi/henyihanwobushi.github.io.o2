---
layout: post
title: "DIY区块链"
date: 2018-08-12 02:10 +0800
---
<!-- TOC -->

- [区块链](#区块链)
    - [区块](#区块)
    - [交易](#交易)
    - [新建区块](#新建区块)
    - [挖矿](#挖矿)
- [API](#api)
    - [交易接口](#交易接口)
    - [挖矿接口](#挖矿接口)
- [一致性](#一致性)
    - [节点记录](#节点记录)
    - [一致性实现](#一致性实现)
- [跑起来](#跑起来)
- [总结](#总结)

<!-- /TOC -->
2018年, 加密货币/区块链曾占据各种头条, 至今尚未停歇, 为什么一盘冷饭会炒这么久, 让人诧异. 没有调查就没有发言权, 今天<b>搬运</b>一个 "learn blockchain the hard way", 学习一下区块链.

<b>注意: </b>

* <b>这篇是我嚼过的, 原文请点击连接: [Learn Blockchains by Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)</b>
* <b>想直接看最终代码的, 点击链接: [blockchain.py](https://github.com/dvf/blockchain/blob/master/blockchain.py)

> [搞一搞]: 这是一个新的尝试, 会自制或者搬运一些有意思的小实验.

## 区块链

区块链包含两个 *list*, 一个存储所有区块(block), 一个存储所有的交易(transaction).

```python
class Blockchain(object):
    def __init__(self):
    	# 所有区块
        self.chain = []
        # 当前交易列表
        self.current_transactions = []
        
    def new_block(self):
        # 创建区块
        pass
    
    def new_transaction(self):
        # 新增交易
        pass
    
    @staticmethod
    def hash(block):
        # 计算hash
        pass

    @property
    def last_block(self):
        # 获取最有一个区块
        pass
```

### 区块

区块包含: 序号, 时间戳, 交易记录, 证明, 上一个块的hash.

区块内包含上一个区块的hash值, 这个特性保证了区块链中保存的交易记录不允许被篡改.

```python
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```

### 交易

每次交易时, 区块链会将交易记录在交易记录里:

```python
class Blockchain(object):
    ...
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
```

### 新建区块

区块链初始化时, 需要新建一个初始区块, 新建区块需要一个 `hash` 函数

```python
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
```

### 挖矿

新增区块(挖矿)当然不是调用一个函数这么简单, 为了保证挖矿的难度需要一个算法, Proof of work: POW. 如下, 找到满足`hash(x*y)` 的最后一个字符为"0", 需要匹配的hash的字符长度越长, 匹配到正确的`y`的难度越大

```python
from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')
```

## API

接下来使用 *Flask* 进行 *API* 封装, 以下是各个接口: 挖矿, 交易, 获取区块列表

```python
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask


class Blockchain(object):
    ...


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"
  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 交易接口

交易接口负责接收交易请求, 并且提交给 `blockchain`, 参数如下:
```json
{
 "sender": "my address",
 "recipient": "someone else's address",
 "amount": 5
}
```

*Flask* 接口代码如下:

```python
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

...

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201
```


### 挖矿接口

挖矿接口主要进行3项工作:
1. 计算工作证明(pow)
1. 增加一笔给自己一个区块的交易
1. 构建新的区块并记录在区块链中

```python
import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

...

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
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
```

## 一致性

以上我们实现了一个单机版的区块链, 可以记录交易, 可以挖矿. 区块链的另一个核心概念是去中心化, 单机不是区块链. 我们需要记录所有的区块链玩家, 并形成互动:

### 节点记录

需要新增节点记录以及解析接口来实现区块链节点之间的互动: `/nodes/register`, `/nodes/resolve`

```python
...
from urllib.parse import urlparse
...


class Blockchain(object):
    def __init__(self):
        ...
        self.nodes = set()
        ...

    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
``` 

### 一致性实现

由于各个节点独立运行, 独立挖矿, 所以难免会存在不一致性, 为修正区块链的不一致性, 规定链条最长的区块链为合法的区块链, 不合法的区块链需要被替换.

```python
...
import requests


class Blockchain(object)
    ...
    
    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False
```

## 跑起来

启动三个区块链程度, 相互注册, 并且进行一些交易和挖矿:

```bash
# 同时启动三个节点
nohup python blockchain.py -p 5000 2>&1 > blockchain.5000.log &
nohup python blockchain.py -p 5001 2>&1 > blockchain.5001.log &
nohup python blockchain.py -p 5002 2>&1 > blockchain.5002.log &

sleep 1
# 节点之间相互注册:
curl -X POST \
  http://localhost:5000/nodes/register \
  -H 'Content-Type: application/json' \
  -d '{"nodes":["http://localhost:5001", "http://localhost:5002"]}'

curl -X POST \
  http://localhost:5001/nodes/register \
  -H 'Content-Type: application/json' \
  -d '{"nodes":["http://localhost:5000", "http://localhost:5002"]}'

curl -X POST \
  http://localhost:5002/nodes/register \
  -H 'Content-Type: application/json' \
  -d '{"nodes":["http://localhost:5001", "http://localhost:5000"]}'

# 交易
curl -X POST \
  http://localhost:5000/transactions/new \
  -H 'Content-Type: application/json' \
  -d '{
 "sender": "bob",
 "recipient": "alice",
 "amount": 5
}'

curl -X POST \
  http://localhost:5000/transactions/new \
  -H 'Content-Type: application/json' \
  -d '{
 "sender": "bob",
 "recipient": "alice",
 "amount": 5
}'

# 挖矿
curl -X GET http://localhost:5000/mine

# 交易
curl -X POST \
  http://localhost:5001/transactions/new \
  -H 'Content-Type: application/json' \
  -d '{
 "sender": "bob",
 "recipient": "alice",
 "amount": 5
}'

# 挖矿
curl -X GET http://localhost:5000/mine
curl -X GET http://localhost:5001/mine

# 查看区块链
curl -X GET http://localhost:5000/nodes/resolve
curl -X GET http://localhost:5001/nodes/resolve
curl -X GET http://localhost:5002/nodes/resolve

```

## 总结

区块链很复杂然而又很简单, 简单到可以用300行写一个 *hello blockchain* 出来, 复杂到一个 *hello blockchain* 竟然需要300行代码.

以上只是简单的示例, 如果要开发一个虚拟货币或者区块链游戏, 还有很多工作要做, 但对不了解区块链的同学来讲是个不错的开始.

----

文章搬运自: [https://hackernoon.com/learn-blockchains-by-building-one-117428612f46](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46), 感谢大神: [Daniel van Flymen](https://hackernoon.com/@vanflymen?source=post_header_lockup)

