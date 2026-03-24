import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    p = np.asarray(p)
    x = np.asarray(x)

    if not np.allclose(np.sum(p), 1):
        raise ValueError("Probabilities don't sum to 1")

    if len(x) == len(p):
        prod = x * p 
        return np.sum(prod) 
    else:
        print("Shapes do not match")
    