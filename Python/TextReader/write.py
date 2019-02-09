from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

TEXT_START_X = 257
TEXT_END_X = 617
TEXT_START_Y = 37
TEXT_END_Y = 225


def write_image(text):
    img = Image.open("black.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 21)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((TEXT_START_X, TEXT_START_Y), text, (255, 255, 255), font=font)
    img.save('black-out.jpg')
