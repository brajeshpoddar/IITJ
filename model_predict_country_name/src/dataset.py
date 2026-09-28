import csv
import torch

def load_dataset(path="data/countries-list.csv"):
    countries = []
    capitals = []

    # Read CSV file
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            countries.append(row["Country"])
            capitals.append(row["Capital"])

    # Build vocabularies
    country_vocab = {c: i for i, c in enumerate(sorted(set(countries)))}
    capital_vocab = {cap: i for i, cap in enumerate(sorted(set(capitals)))}

    # Convert to tensors
    X = torch.tensor([country_vocab[c] for c in countries], dtype=torch.long)
    y = torch.tensor([capital_vocab[cap] for cap in capitals], dtype=torch.long)

    return X, y, country_vocab, capital_vocab
