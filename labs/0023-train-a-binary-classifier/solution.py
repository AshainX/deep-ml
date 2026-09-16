import numpy as np
#from sklearn.linear_model import LogisticRegression

# You can import any sklearn module you need

def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z))

def train(X_train, y_train, X_val, y_val):
    """
    Train a binary classifier.
    
    Args:
        X_train: numpy array of shape (n_samples, 30) -- standardized features
        y_train: numpy array of shape (n_samples,) -- binary labels (0 or 1)
        X_val:   numpy array of shape (n_val, 30) -- standardized
        y_val:   numpy array of shape (n_val,) -- validation labels
    
    Returns:
        predict: callable that takes X (n, 30) and returns y_pred (n,) of 0s and 1s
    """
    X = np.vstack([X_train, X_val])
    y = np.concatenate([y_train, y_val])
    
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0
    
    lr = 0.1
    epochs = 400
    
    for _ in range(epochs):
        z = np.dot(X, w) + b
        y_hat = sigmoid(z)
        
        dz = y_hat - y
        dw = (1.0 / n_samples) * np.dot(X.T, dz)
        db = (1.0 / n_samples) * np.sum(dz)
        
        w -= lr * dw
        b -= lr * db
    
    def predict(X_test):
        z_test = np.dot(X_test, w) + b
        probs = sigmoid(z_test)
        return (probs >= 0.5).astype(int)

    return predict
    
    #pass
