import torch
import torch.nn as nn
import torch.optim as optim
from dataset import load_dataset
from model import CountryCapitalModel

# Load data
X, y, country_vocab, capital_vocab = load_dataset("data/countries-list.csv")

# Model setup
model = CountryCapitalModel(vocab_size=len(country_vocab)+1, embed_dim=16, num_capitals=len(capital_vocab))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(200):
    total_loss = 0
    for inp, tgt in zip(X, y):
        output = model(inp.unsqueeze(0))   # add batch dimension
        loss = criterion(output, tgt.unsqueeze(0))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.4f}")

# Save model
torch.save({
    "model_state": model.state_dict(),
    "country_vocab": country_vocab,
    "capital_vocab": capital_vocab
}, "models/country_capital.pth")

print("Model trained and saved to models/country_capital.pth")
