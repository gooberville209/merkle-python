Initialization: The MerkleTree class is initialized with a list of data.
Leaf Hashing: Each piece of data is hashed to create the leaves of the tree.
Node Hashing: Internal nodes are created by hashing the concatenation of the hashes of the child nodes.
Tree Building: The tree is built recursively by combining nodes until a single root hash is obtained.
Usage: The example usage demonstrates creating a Merkle tree from a list of data and printing the root hash.
