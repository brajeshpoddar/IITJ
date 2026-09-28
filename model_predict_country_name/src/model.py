import torch
import torch.nn as nn

class CountryCapitalModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_capitals):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, num_capitals)

    def forward(self, x):
        x = self.embedding(x)          # country → vector
        x = x.mean(dim=0, keepdim=True)
        return self.fc(x)              # predict capital class
