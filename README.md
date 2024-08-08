	1.	Initialization: The MerkleTree class is initialized with a list of data.
	2.	Leaf Hashing: Each piece of data is hashed to create the leaves of the tree.
	3.	Node Hashing: Internal nodes are created by hashing the concatenation of the hashes of the child nodes.
	4.	Tree Building: The tree is built recursively by combining nodes until a single root hash is obtained.
	5.	Usage: The example usage demonstrates creating a Merkle tree from a list of data and printing the root hash.
