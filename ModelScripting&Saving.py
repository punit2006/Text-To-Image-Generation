# Script and save model
scripted_model = torch.jit.script(model)
print(scripted_model)
scripted_model.save("scripted_model.pt")

# Load model
loaded_model = torch.jit.load("scripted_model.pt")
print(loaded_model)
