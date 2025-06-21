import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

# Initialize pipeline
authorization_token = "YOUR_TOKEN_HERE"
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", 
                                             torch_dtype=torch.float16, 
                                             use_auth_token=authorization_token)
pipe.to(device)

# Generate image
with autocast(device):
    textprompt = str(input("Enter Your prompt: "))
    image = pipe(textprompt, guidance_scale=8.5).images[0]
    imgplot = plt.imshow(image)
