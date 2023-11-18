# 이미지에서 텍스트 데이터 추출 및 위치 정보 반환
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang='kor')
# 문자열의 좌상단 좌표와 우하단 좌표 초기화
top_left = [0]*2
bottom_right = [0]*2
flag=0
flagb=0
# 추출된 데이터에서 특정 문자열의 좌상단 좌표와 우하단 좌표 찾기
for i in range(len(data['text'])):
    text = data['text'][i]
    left = data['left'][i]
    top = data['top'][i]
    width = data['width'][i]
    height = data['height'][i]

    # 문자열이 일치하는 경우
    if target_string_start in text:
        if flag == 0:
            flag = 1
            top_left[0] = left
            top_left[1] = top

    if target_string_end in text:
        if flagb==0:
            flagb=1
            bottom_right[0] = left + width
            bottom_right[1] = top + height
mosaic_region = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
draw = ImageDraw.Draw(output_image)
draw.rectangle(mosaic_region, fill=color, outline=color, width=2)

# 결과 이미지 저장
output_image.save(output_image_path)
return None
