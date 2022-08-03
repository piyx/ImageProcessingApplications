import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color

from skimage.util import random_noise
from skimage.restoration import denoise_tv_chambolle

import requests
import os
import json

import subprocess



def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    

    
def denoise_image(base_path, relative_path):
    import os
    full_path = f"{base_path}{relative_path}"
    path, ext = os.path.splitext(relative_path)
    input_image = plt.imread(full_path)
    denoised = denoise_tv_chambolle(input_image)
    output_path = f"{base_path}{path}_output{ext}"
    plt.imsave(output_path, denoised, cmap='gray')
    return f"{path}_output{ext}"



def restore_image(base_path, relative_path):
    full_path = f"{base_path}{relative_path}"
    link = subprocess.check_output(f"curl --upload-file {full_path} https://free.keep.sh", shell=True)
    link = str(link.decode('utf-8')).strip('\n')
    payload = {"input": {"image": f"{link}/download","HR": "true","with_scratch": "true"}}
    url = "http://localhost:5000/predictions"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.json()["output"][0]["file"]