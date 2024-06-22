import requests
import torch
import clip

from PIL import Image
from io import BytesIO
from .dataset import device, model, preprocess


def fetch_encode_image(item):
    """Fetch and embed images"""
    img_url = item.get("images")[0]
    res = requests.get(img_url, verify=False)
    img = Image.open(BytesIO(res.content))
    img = preprocess(img).unsqueeze(0).to(device)  # type: ignore
    with torch.no_grad():
        image_features = model.encode_image(img)
    return image_features.cpu().numpy().flatten()


def encode_text(text):
    """Tokenize image's text and queries"""
    text = clip.tokenize([text]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text)
    return text_features.cpu().numpy().flatten()
