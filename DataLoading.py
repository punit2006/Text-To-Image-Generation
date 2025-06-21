from torch.utils.data import DataLoader, TensorDataset

# Create dataset
data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
targets = torch.tensor([[1.0], [0.0]])
dataset = TensorDataset(data, targets)

# Create data loader
loader = DataLoader(dataset, batch_size=1, shuffle=True)
for batch in loader:
    print(batch)
