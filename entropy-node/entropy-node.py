import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    unique_elements, counts = np.unique(y, return_counts=True)
    if len(counts) <= 1:
        return 0.0

    total_count = len(y)
    probablities = counts / total_count
    probablities_filtered = probablities[probablities > 0]

    '''entropy = 0
    for i in range(len(probablities)):
        if not probablities[i] == 0:
            entropy += (-probablities[i] * np.log2(probablities[i]))
            print("IF ", entropy)
        else:
            entropy += (-probablities[i])
            print("Else ", entropy)
    '''
    
    entropy = -np.sum(probablities_filtered * np.log2(probablities_filtered))
    
    return entropy