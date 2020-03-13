### Explain in detail the workings of a dynamic array:
A dynamic array is an array with an automatic resizing. It is an array that expands as you add more elements to it. So, you don't need to determine the size ahead of time.

### What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

- Add or remove from the front: 0(n)
- Add or remove from the back: 0(1)

### What is the worse case scenario if you try to extend the storage size of a dynamic array?
O(n)

### Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?


Blockchain is a data structure that’s useful for sharing a ledger of transactions that is universally agreed upon, but without the need for a central authority. It forms the basis for cryptocurrency, and is useful in a variety of different fields, including voting, contracts, and many others.

The blockchain is like a linked list in the context of data structures. 

Blockchains are composed of three core parts:

- Block:  A list of transactions recorded into a ledger over a given period. The size, period, and triggering event for blocks is different for every blockchain.
- Chain: A hash that links one block to another, mathematically “chaining” them together.
- Network: The network is composed of “full nodes.” Each node contains a complete record of all the transactions that were ever recorded in that blockchain.

### Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

In Blockchain, proof of work(PoW) is used to confirm transactions and produce new blocks to the chain.
With PoW, miners compete against each other to complete transactions on the network and get rewarded.

##### How does it work?
Miners compete against each other in solving complex computational puzzles. These puzzles are difficult to solve, but when solved, the solutions can be quickly verified. So, once a miner finds the solution to a new block, they can broadcast that block to the network. All other miners will then verify that the solution is correct and the block will likely be confirmed.

