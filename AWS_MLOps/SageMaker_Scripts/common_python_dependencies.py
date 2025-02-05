## Common dependencies for using Python in SageMaker

%%capture 
!pip install einops

%%capture 
!pip install --upgrade pandas fsspec # sagemaker dependency

%%capture 
!pip install seaborn
!pip install s3fs #sagemaker dependency


%%capture  
## upgrade accelerate to use device_map 
!pip install --upgrade accelerate ## this is for compatability with `bitsandbytes` 


## check accelerate version after upgrade
import accelerate
print(f"Accelerate version: {accelerate.__version__}") 


%%capture
!pip install bertopic datasets bitsandbytes xformers adjustText # make sure to install ALL


%%capture 
## upgrade torchvision
!pip install --upgrade torchvision # if you need to upgrade torchvision run this line
!pip install --upgrade torch #upgrade torch version


# check versions of torch available
import torch
import torchvision 

# print versions
print(f"PyTorch version: {torch.__version__}") 
print(f"Torchvision version: {torchvision.__version__}")


# check if GPU is available 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
print(f"Using device: {device}")

# set device for PyTorch operations
if device.type == "cuda":
    torch.cuda.set_device(0) # you can use a different device ID if you have multiple GPUs running


## standard Data Science imports
import pandas as pd
import numpy as np

## plotting
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import HTML
import seaborn as sns

## other tools
#import response_compare
import re
import functools
from copy import deepcopy
import chardet
import html #for non ascii detection

## transformers and huggingface
import transformers
#from sentence_transformers import SentenceTransformer, util
import torch
import torchvision ## to use Qwen
import huggingface_hub

## tqdm and pandas
from tqdm.auto import tqdm
tqdm.pandas(leave=False)
#from hashlib import sha256


## hf hub login
from huggingface_hub import notebook_login
notebook_login()
