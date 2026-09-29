import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """

    lr = 0.05
    epoch = 1000
    n = len(X)

    for _ in range(epoch):
        ypred = X @ W + b
        err = ypred - y
        dw = (X.T @ err)/n
        db = np.mean(err)

        W = W -lr *dw
        b = b -lr *db

    return W, float(b)
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    #pass
