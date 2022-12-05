# from PIL import Image, ImageDraw, ImageFont
# inm = "Aaa.jpg"
# img = Image.open(inm)
# d = ImageDraw.Draw(img)
# fnt = ImageFont.truetype=("comicbd.ttf" , 10)
# d.text((60 , 60) , "seam" , font=fnt , fill=(255 , 255, 255))
# img.save('bb.jpg')
# d.text()
import os
import sys
from PIL import Image, ImageDraw, ImageFont
def logo():
    
    seam = input("ENter you name")
    # get an image
    with Image.open("gg.png").convert("RGBA") as base:

     # make a blank image for the text, initialized to transparent text color
     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

     # get a font
     fnt = ImageFont.truetype("ss.ttf", 40)
     # get a drawing context
     d = ImageDraw.Draw(txt)

    
   
     # draw text, full opacity
     d.text((10, 60), seam, font=fnt, fill=(255, 255, 255, 255))
    
    
     out = Image.alpha_composite(base, txt)
     out.save('bb.png')
    os.system("clear")
    
if __name__ == "__main__":
    logo() 