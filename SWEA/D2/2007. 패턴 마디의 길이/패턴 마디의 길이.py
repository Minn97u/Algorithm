def find_repeating_word(sentence):
    # 반복 단어의 최대 길이는 30의 절반인 15까지 가능
    for length in range(1, 16):  # 길이를 1부터 15까지 시도
        word = sentence[:length]  # 문자열의 처음부터 길이만큼 단어 추출
        repeated = word * (30 // length)  # 단어를 전체 길이에 맞게 반복
        if sentence.startswith(repeated):  # 원래 문자열이 반복된 문자열로 시작하면
            return word
    return "반복 단어 없음"

# 입력 받기
T = int(input())
for i in range(1, T+1):
    sentence = input().strip()  # 공백 제거
    result = find_repeating_word(sentence)
    print(f"#{i} {len(result)}")