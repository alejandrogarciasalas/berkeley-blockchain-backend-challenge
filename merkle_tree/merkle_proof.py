from utils import *


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    "*** YOUR CODE HERE ***"    
    if (merkle_tree.block_header == hash_data(tx + tx)):
        return []

    if len(merkle_tree.leaves) > 0:
        levels = [merkle_tree.leaves, ]
        while len(levels[0]) > 1:
            new_level = []
            for left, right in \
                zip(levels[0][0:len(levels[0]):2], levels[0][1:len(levels[0]):2]):
                new_level.append(hash_data(left + right))
            levels = [new_level, ] + levels

    index = merkle_tree.leaves.index(tx)

    proof = []
    for i in range(len(levels) - 1, 0, -1):
        if (index == len(levels[i]) - 1) and (len(levels[i]) % 2 == 1):
            index = int(index / 2)
            continue

        if index % 2: # right node
            sibling_index = index - 1
        else:
            sibling_index = index + 1

        proof.append(levels[i][sibling_index])
        index = int(index / 2)

    return proof[::-1]

def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    "*** YOUR CODE HERE ***"
    proof = merkle_proof[::-1]
    verified_hash = hash_data(tx + proof[0])
    for p in proof[1:]:
        verified_hash = hash_data(verified_hash + p)
    return verified_hash
