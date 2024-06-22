import os
import json
import torch
import clip
import ssl
import urllib.request

# ssl configuration
ssl._create_default_https_context = ssl._create_unverified_context


def _download(url, download_root):
    """Function to override _download in clip"""
    filename = os.path.basename(url)
    download_target = os.path.join(download_root, filename)

    with urllib.request.urlopen(url) as source, open(download_target, "wb") as output:
        output.write(source.read())
    return download_target


clip._download = _download  # type: ignore

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

dataset = os.path.join("./db/products.json")
with open(dataset, "r") as file:
    dataframe = json.load(file)
