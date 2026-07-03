import numpy as np

import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    mx = (max(len(seq) for seq in seqs) if max_len == None else max_len)
    sol = np.zeros((len(seqs), mx), dtype=np.int32)

    # print(sol.shape)
    # print(mx)

    for i in range(0, len(seqs)):
        m = len(seqs[i])
        sq_copy = np.array(seqs[i])
        if (m < mx):
            sq_copy = np.pad(
                sq_copy,
                (0, mx - m),
                mode='constant',
                constant_values=pad_value
            )
        else :
            sq_copy = sq_copy[0:mx]
        sol[i] = sq_copy[:mx]

    return sol
