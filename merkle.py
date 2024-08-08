import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.leaves = [self.hash_leaf(data) for data in data_list]
        self.root = self.build_tree(self.leaves)

    @staticmethod
    def hash_leaf(data):
        return hashlib.sha256(data.encode()).hexdigest()

    @staticmethod
    def hash_node(left, right):
        return hashlib.sha256((left + right).encode()).hexdigest()

    def build_tree(self, leaves):
        if len(leaves) == 1:
            return leaves[0]
        
        new_level = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i + 1] if i + 1 < len(leaves) else left
            new_level.append(self.hash_node(left, right))
        
        return self.build_tree(new_level)

    def get_root(self):
        return self.root

# Example usage
if __name__ == "__main__":
    data_list = ["data1", "data2", "data3", "data4"]
    merkle_tree = MerkleTree(data_list)
    print("Root hash:", merkle_tree.get_root())
