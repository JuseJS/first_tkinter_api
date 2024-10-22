from PIL import Image, ImageTk
import requests
from io import BytesIO

class ImgController:
    @staticmethod
    def download_image(url, size=(150, 150)):
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))
        image_data = image_data.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image_data)