import tkinter
from PIL import Image, ImageTk, ImageFont, ImageDraw

logo = Image.open("Logo Watermark.png")

logo_no_background = Image.open("Watermark Logo No BackGround.png")


class WaterMarker():
    def __init__(self):
        self.logo = logo
        self.logo_no_background = logo_no_background
        self.initials = "KD"


    def set_wtr_mark(self, radio_value):
        """Scans the users radio input and selects the appropriate choice of watermark"""
        mark = self.logo
        print (f"1st method called {radio_value}")
        if radio_value == 1:
            mark = self.logo
        elif radio_value == 2:
            mark = self.logo_no_background
        elif radio_value == 3:
            mark = self.initials
        return mark

    def mark_img(self, radio_value, base_img):
        """Applies the chosen watermark to the image"""
        print(f"Function called {radio_value}")
        base_img = Image.open(base_img)
        base_width, base_height = base_img.size
        thumbnail_size = (int(base_width / 10), int(base_height / 10))

        if radio_value == 1:
           mark = self.logo
           mark.thumbnail(thumbnail_size)
           copy = base_img.copy()
           copy.paste(mark, (base_width - int(base_width / 5), base_height - int(base_height / 5)))
           copy.save("watermarked_img.png", "PNG")

        if radio_value == 2:
            mark = self.logo_no_background
            mark.thumbnail(thumbnail_size)
            copy = base_img.copy()
            copy.paste(mark, (base_width - int(base_width / 5), base_height - int(base_height / 5)))
            copy.save("watermarked_img.png", "PNG")
            #follow procedure for marking with an image

        elif radio_value == 3:
            print("Picked up on Radio 3")
            copy = base_img.copy()
            draw = ImageDraw.Draw(copy)
            font_size = int(base_width / 8)
            font = ImageFont.truetype('arial.ttf', font_size)
            x, y = int(base_width - (base_width / 5)), int(base_height - (base_height/5))
            draw.text((x, y), self.initials, font=font, fill=(0, 0, 0))
            copy.save("watermarked_img.png", "PNG")






