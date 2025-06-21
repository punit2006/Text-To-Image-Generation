!pip install torch diffusers matplotlib transformers accelerate
import torch

# Basic tensor operations
x = torch.tensor([1.0,2.0,3.0])
y = torch.ones(3)
z = x + y
print(z)

# Tensor properties
print(x.shape, x.size(), x.dtype)

# GPU operations
device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
x = x.to(device)

# Autograd example
x = torch.tensor(3.0, requires_grad = True)
y = x ** 2
y.backward()
print(x.grad)
