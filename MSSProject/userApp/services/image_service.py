from PIL import Image


class ImageService:
    def resize_image(self, image_path: str):
        img = Image.open(image_path).convert("RGB")
        img = img.resize((340, 300), Image.Resampling.LANCZOS)
        img.save(image_path)
