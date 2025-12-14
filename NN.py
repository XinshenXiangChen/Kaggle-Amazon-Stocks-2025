import torch.nn as nn
from torch.nn import Sequential

class NN(nn.Module):
    def __init__(self):
        super(NN, self).__init__()

        self.network = Sequential()

    def forward(self, x):
        pass