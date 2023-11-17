#이미지 처리하는 pillow 라이브러리 불러오기
from PIL import Image

#Tesseract 라이브러리 불러오기
import pytesseract
import re

#이미지(경로) 선택
image_path = r"C:\Users\SUN\Documents\OCR PHOTOS\메모장7.PNG"

#Tesseract 파일 위치
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#text 변수에 OCR 결과 저장
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

# new_text = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z-\s]", "", text)
# new_text = new_text.replace(" ", "")
print(text)