input_value=input()
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
    if val != d[12]:
        return False
    return True  # 검증코드 확인
print(validate_resident_number(0))