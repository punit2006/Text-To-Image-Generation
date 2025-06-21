import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1,1)
    
    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

# Training loop
for epoch in range(10):
    optimizer.zero_grad()
    output = model(torch.tensor([[1.0]]))
    loss = criterion(output, torch.tensor([[1.0]]))
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch}, Loss: {loss.item()}")
