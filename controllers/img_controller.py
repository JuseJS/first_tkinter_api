import asyncio
import aiohttp
from PIL import Image, ImageTk
from io import BytesIO
import threading

class ImgController:
    @staticmethod
    async def download_image_async(url, size=(300, 300)):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    image_data = Image.open(BytesIO(await response.read()))
                    image_data = image_data.resize(size, Image.Resampling.LANCZOS)
                    return ImageTk.PhotoImage(image_data)
        except Exception as e:
            print(f"Fallo al descargar la imagen con url: {e}")
            return None

    @staticmethod
    def update_image_label(label, url, size=(300, 300)):
        def run_update():
            asyncio.run(ImgController._update_image(label, url, size))

        if not asyncio.get_event_loop().is_running():
            threading.Thread(target=run_update, daemon=True).start()
        else:
            asyncio.create_task(ImgController._update_image(label, url, size))

    @staticmethod
    async def _update_image(label, url, size):
        new_image = await ImgController.download_image_async(url, size)
        if new_image:
            label.config(image=new_image)
            label.image = new_image
