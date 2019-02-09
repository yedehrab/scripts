# Gereklilikler
# conda install -c mcs07 tesseract
# conda install -c jim-hart pytesseract

# Türkçe dili eklemek için:
# https://github.com/tesseract-ocr/tessdata/raw/3.04.00/tur.traineddata
# image_to_string(img, lang="tur") yazdığınızda hatanın geldiği yola kopyalayın.

from PIL import Image
from pytesseract import image_to_string
import write

IMAGE_PATH = "./test2.jpg"

img = Image.open(IMAGE_PATH)
text = image_to_string(img, lang="tur")

write.write_image(text)
