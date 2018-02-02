import numpy as np
import matplotlib.pyplot as plt

from bp import Sigmoid,MSE,Linear,CrossEntropy,Softmax

from utils import sanity_check

def test_Linear():
    layer = Linear(2,10)
    x = np.random.uniform(size=(2,2))
    sanity_check(layer,x)

def test_Sigmoid():
    layer = Sigmoid()
    x = np.random.uniform(size=(2,2))
    sanity_check(layer,x)

def test_MSE():
    layer = MSE()
    x = np.random.uniform(size=(2,2))
    sanity_check(layer,x,np.zeros(x.shape))

def test_CrossEntropy():
    layer = CrossEntropy()
    x = np.random.uniform(size=(2,2))
    sanity_check(layer,x,np.ones(x.shape))

def test_Softmax():
    layer = Softmax()
    x = np.random.uniform(size=(2,2))
    sanity_check(layer,x)

def main():
    test_Linear()
    test_MSE()
    test_Sigmoid()
    test_Softmax()

if __name__ == "__main__":
    main()