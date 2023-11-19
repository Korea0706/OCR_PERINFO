import re
from PIL import Image, ImageDraw
import pytesseract

image_path = r"C:\Users\SUN\Documents\OCR PHOTOS\메모장16.PNG" #이미지 입력
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
input_value = pytesseract.image_to_string(Image.open(image_path), lang="kor")
input_value = input_value.replace(" ", "")
input_value = input_value.replace("\n", "")
image = Image.open(image_path)
output_image_path = r"C:\Users\SUN\Documents\OCR PHOTOS\mosaic.PNG"
output_image = image.copy()


names = ['민준', '서준', '도윤', '예준', '시우', '하준', '지호', '주원', '지후', '준우', '준서', '도현', '건우', '현우', '우진', '지훈', '선우', '유준', '서진', '연우', '은우', '민재', '현준', '시윤', '정우', '이준', '승우', '윤우', '지환', '지우', '승현', '유찬', '준혁', '수호', '승민', '시후', '진우', '민성', '수현', '준영', '지원', '이안', '재윤', '시현', '태윤', '한결', '지안', '동현', '윤호', '시원', '은찬', '시온', '민우', '재원', '민규', '지한', '서우', '은호', '재민', '민찬', '우주', '우빈', '하율', '준호', '지율', '성민', '하진', '승준', '성현', '재현', '현서', '민호', '태민', '예성', '지성', '지민', '윤재', '태현', '민혁', '하람', '규민', '성준', '하민', '로운', '윤성', '정민', '태양', '이현', '은성', '예찬', '준수', '도훈', '준희', '민석', '다온', '주안', '주호', '서윤', '서연', '지우', '서현', '하윤', '하은', '민서', '지유', '윤서', '채원', '수아', '지민', '지아', '지윤', '다은', '은서', '예은', '지안', '소율', '서아', '예린', '수빈', '하린', '소윤', '예원', '지원', '유나', '시은', '채은', '유진', '윤아', '예나', '가은', '시아', '아린', '예서', '서영', '연우', '예진', '민지', '주아', '하율', '수민', '다인', '수연', '유주', '아윤', '연서', '서우', '아인', '시연', '서은', '다연', '채윤', '나은', '서율', '하연', '나윤', '지율', '현서', '서하', '서진', '유빈', '다현', '채아', '예지', '수현', '소은', '사랑', '나연', '지은', '시현', '예빈', '민주', '은채', '세아', '윤지', '소연', '지현', '다윤', '주하', '지수', '승아', '소민', '혜원', '채린', '다온', '하영', '민아', '나현', '서희', '세은', '아영', '도연', '규리', '이서', '가윤', '유하', '아현', '연아']
THREEDATA = ["경기도", "기장군","강남구","강동구","강북구","권선구","강서구","영통구","달성군","관악구","장안구","군위군","광진구","팔달구","수원시","구로구","성남시","금천구","노원구",
"안양시","울주군","도봉구","분당구","부천시","수정구","광명시","동작구","중원구","평택시","마포구","강화군","안산시","옹진군","서초구","동안구","고양시","성동구","만안구","과천시","성북구",
"구리시","송파구","연천군","양천구","덕양구","오산시","가평군","시흥시","양평군","용산구","군포시","은평구","의왕시","종로구","하남시","단원구","용인시","홍천군","중랑구","상록구","파주시",
"횡성군","이천시","영월군","안성시","평창군","강서구","기흥구","김포시","정선군","금정구","수지구","화성시","철원군","처인구","광주시","화천군","양주시","양구군","동래구","포천시","인제군",
"원미구","여주시","고성군","소사구","춘천시","양양군","사상구","오정구","원주시","사하구","강릉시","동해시","수영구","청주시","태백시","보은군","연제구","속초시","옥천군","영도구","상당구","삼척시","영동군","흥덕구","청주시","증평군","청원구","충주시","진천군","서원구","제천시","괴산군","천안시","음성군","공주시","단양군","보령시","천안시","아산시","연수구","서산시","남동구","동남구","논산시","금산군","부평구","서북구","계룡시","부여군","계양구","당진시","서천군","전주시","청양군","군산시","홍성군","전주시","익산시","예산군","정읍시","태안군","달서구","덕진구","남원시","당진시","완산구","김제시","연기군","목포시","여수시","수성구","순천시","포항시","나주시","완주군","광양시","진안군","포항시","무주군","광산구","경주시","장수군","김천시","임실군","안동시","순창군","구미시","고창군","창원시",
"영주시","부안군","의창구","상주시","대덕구","성산구","문경시","경산시","담양군","창원시","곡성군","유성구","진해구","진주시","구례군","통영시","고흥군","사천시","보성군","김해시","화순군","밀양시","장흥군","거제시","강진군","양산시","해남군","제주시","영암군","무안군","함평군","영광군","장성군","완도군","진도군","신안군"]
FOURDATA = ["의정부시","동대문구","동두천시","서대문구","남양주시","영등포구","일산동구","일산서구","부산진구","해운대구","미추홀구","서귀포시"]
FIVEDATA = ["서울특별시","부산광역시","대구광역시","인천광역시","대전광역시","광주광역시","울산광역시","마산합포구","마산회원구"]
SEVENDATA = ["세종특별자치시"]

def mosaic(target_string_start, target_string_end, color):

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

def chnm(d):
    d = re.sub(r'[a-z0-9-_.]+','', d)
    if len(d) < 2:
        return
    for j in range(0, len(d)-1, 1):
        w = d[j:j + 2]
        if w in names:
            print(f"{w} 이름임")
            mosaic(d[j-1], d[j + 1], 'purple')
def validate_resident_number(a):
    for i in range(a,a+13):
        if i == a+6:
            if input_value[i] != '-':  # 번호에 '-'가 없으면 개인정보 아님
                return False
        else:
            if not input_value[i].isdigit():
                return False  # 모든 문자열이 숫자가 아니라면 개인정보가 아님
    d = [0] * 13
    for i in range(13):
        if i < 6:
            d[i] = int(input_value[i])
        else:
            d[i] = int(input_value[i + 1])  # 13자리(주민번호)를 리스트화 시킴
    if d[2] >= 2:
        return False  # 3번째 자리가 2 이상이면 개인정보 아님
    if d[4] >= 4:
        return False  # 5번째 자리가 4 이상이면 개인정보 아님
    if d[6] >= 9:
        return False  # 7번째 자리가 9 이상이면 개인정보 아님
    val = 0
    mult = 2
    for i in range(12):
        val += d[i] * mult
        mult += 1
        if mult > 9:
            mult = 2
    val %= 11
    val = 11 - val
    val %= 10
    if val != d[12]:
        return False
    return True  # 검증코드 확인
    pass

def ch(s):
    s = re.sub(r'[a-z0-9-_.]+', '', s)
    if len(s) < 3:
        return
    for j in range(0, len(s)-2, 1):
        w = s[j:j+3]
        if w in THREEDATA:
            print(f"{w} 주소임")
            mosaic(s[j], s[j+2], 'green')

    if len(s) < 4:
        return
    for j in range(0, len(s)-3, 1):
        w = s[j:j+4]
        if w in FOURDATA:
            print(f"{w} 주소임")
            mosaic(s[j], s[j + 3], 'green')
    if len(s) < 5:
        return
    for j in range(0, len(s)-4, 1):
        w = s[j:j+5]
        if w in FIVEDATA:
            print(f"{w} 주소임")
            mosaic(s[j], s[j + 4], 'green')
    if len(s) < 7:
        return
    for j in range(0, len(s)-6, 1):
        w = s[j:j+7]
        if w == SEVENDATA:
            print(f"{w} 주소임")
            mosaic(s[j], s[j + 6], 'green')
while True:
    qusn = input('개인정보가 발견되면 가릴까요?(Y/N) ')
    if qusn == 'Y':
        while True:
            ans = input('가리고 싶은 문자열이 있나요? (Y/N) ')
            if ans == 'Y':
                input_value3 = input("가리고 싶은 특정 문자 : ")
                if input_value3 in input_value:
                    print(f"{input_value3} : 발견됨")
                    mosaic(input_value3[0], input_value3[len(input_value3) - 1], 'teal')
                    break
            elif ans == 'N':
                pass
                break
            else:
                print("Y 또는 N을 입력해주세요.")
        input_value = re.sub(r"[a-zA-Z]", "", input_value)
        input_value2 = input_value
        input_value = re.sub(r"[ㄱ-ㅣ가-힣]", "", input_value)
        input_value2 = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", input_value2)

        ch(input_value2)
        chnm(input_value2)

        # Check for personal information in input
        for i in range(len(input_value)-13):
            # Check for Korean resident registration numbers
            if validate_resident_number(i):
                print(input_value[i:i + 14], ": 주민등록번호임")
                mosaic(input_value[i:i+14], input_value[i:i + 14], 'red')

        # 이미지 뷰어로 결과 확인
        output_image.show()
        break

    elif qusn == 'N':
        pass
        break
    else:
        print("Y 또는 N을 입력하세요.")
