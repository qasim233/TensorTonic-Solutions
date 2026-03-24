def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    relevant = set(relevant)

    common_count = len(set(top_k).intersection(relevant))

    precision = common_count / k 
    recall = common_count / len(relevant)

    return [precision, recall]