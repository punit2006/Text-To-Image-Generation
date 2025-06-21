# Text-To-Image-Generation

# PyTorch & Matplotlib Repository  

🚀 **A collection of practical examples showcasing PyTorch and Matplotlib for deep learning, tensor operations, and data visualization.**  

This repository provides hands-on implementations of:  
- **PyTorch fundamentals** (tensors, autograd, GPU operations)  
- **Neural network training** (model definition, loss functions, optimization)  
- **Data loading & batching** with `TensorDataset` and `DataLoader`  
- **Model scripting & deployment** using TorchScript  
- **Matplotlib visualizations** (line plots, bar charts, scatter plots)  
- **Stable Diffusion** image generation with Hugging Face's `diffusers`  

---

## 📌 **Key Features**  

### **1. PyTorch Basics**  
- Tensor operations and properties  
- Automatic differentiation with `autograd`  
- GPU/CPU device management  

### **2. Neural Network Training**  
- Custom `nn.Module` implementation  
- Training loop with `MSELoss` and SGD optimizer  

### **3. Data Handling**  
- Creating datasets with `TensorDataset`  
- Batching and shuffling with `DataLoader`  

### **4. Model Export & Deployment**  
- Scripting models with `torch.jit.script`  
- Saving & loading models in `.pt` format  

### **5. Data Visualization**  
- Line plots, bar charts, and scatter plots  
- Custom styling (colors, markers, linestyles)  

### **6. Stable Diffusion (Bonus)**  
- Text-to-image generation using Hugging Face's `diffusers`  
- GPU-accelerated inference with mixed precision (`fp16`)  

---

## 🛠 **Installation**  

```bash
pip install torch diffusers matplotlib transformers accelerate
```

## 🏃 **Quick Start**  

1. **Run PyTorch examples:**  
   ```python
   python pytorch_basics.py
   ```
2. **Train a simple neural network:**  
   ```python
   python train_model.py
   ```
3. **Generate plots:**  
   ```python
   python matplotlib_plots.py
   ```
4. **Try Stable Diffusion (requires GPU & Hugging Face token):**  
   ```python
   python stable_diffusion.py
   ```

---

## 📂 **Repository Structure**  

```
├── pytorch_basics.py          # Tensor ops, autograd, GPU usage  
├── train_model.py            # Neural network training loop  
├── data_loading.py           # Dataset & DataLoader examples  
├── model_export.py           # TorchScript model scripting  
├── matplotlib_plots.py       # Visualization examples  
├── stable_diffusion.py       # Text-to-image generation  
├── README.md                 # This file  
└── requirements.txt          # Dependencies  
```

## 🤝 **Contributing**  
Feel free to open issues or PRs for improvements!  

⭐ **Star this repo if you find it useful!** ⭐  

🔗 **Connect with me:**  
[GitHub](https://github.com/punit2006) | [LinkedIn](https://linkedin.com/in/punitjain163)  

**Here's the ColabLink**
https://colab.research.google.com/drive/1HuHYzOzCBcb1YWKIL_wpldh_Octp8ElR?usp=sharing
