from PIL import Image


class ImageService:
    def resize_image(self, image_path: str):
        basewidth = 300
        img = Image.open(image_path)
        wpercent = basewidth / float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        img.save(image_path)
