import torch
from model import CountryCapitalModel

# Load saved model + vocabs
checkpoint = torch.load("models/country_capital.pth")
country_vocab = checkpoint["country_vocab"]
capital_vocab = checkpoint["capital_vocab"]

model = CountryCapitalModel(vocab_size=len(country_vocab)+1, embed_dim=16, num_capitals=len(capital_vocab))
model.load_state_dict(checkpoint["model_state"])
model.eval()

# Reverse lookup for capitals
capital_lookup = {idx: cap for cap, idx in capital_vocab.items()}

def predict_capital(country_name):
    if country_name not in country_vocab:
        return "Unknown country"
    inp = torch.tensor([country_vocab[country_name]])
    output = model(inp)
    predicted = torch.argmax(output, dim=1).item()
    return capital_lookup[predicted]

# Example usage
print("India →", predict_capital("India"))
print("France →", predict_capital("France"))
