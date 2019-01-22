import codecs
import re
import datetime
import pickle

# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def make_dict() :
    start = datetime.datetime.now()
    print("사전 만드는 중... ( "+str(start)+" )")

    # 저장소 설정
    dataW = open('dictionary.pickle','wb')

    # 가사 파일 열기
    input_file = "lyrics.txt"
    fp = codecs.open(input_file, 'r', encoding='utf-8')
    text = fp.read()
    fp.close()

    # 불필요한 성분 제거
    text = text.replace('\ufeff','')
    text = text.strip()
    text = text.replace("\r\n","\n")
    lines = text.split("\n")

    # 자료형을 딕셔너리로 설정. 따로 중복값 제거 안해줘도 되므로
    word_list = {}

    for line in lines:
        inputs = line.split(" ")

        for input in inputs:
            input = input.strip()

            # 숫자나 공백, 한문 같은거 걸러냄. 오직 한글만 match
            if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', input) is None:
                continue

            split_keyword_list = list(input)
            cha = []
            for keyword in split_keyword_list:
                # 한글 여부 check 후 분리
                if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*', keyword) is not None:
                    char_code = ord(keyword) - BASE_CODE
                    char1 = int(char_code / CHOSUNG)
                    char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
                    char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))

                    if JONGSUNG_LIST[char3] == ' ':
                        cha.append(CHOSUNG_LIST[char1] + JUNGSUNG_LIST[char2] + "P")
                    else:
                        cha.append(CHOSUNG_LIST[char1]+JUNGSUNG_LIST[char2]+JONGSUNG_LIST[char3])
            word_list[input]=" ".join(cha)

    pickle.dump(word_list,dataW,pickle.HIGHEST_PROTOCOL)
    print("총 "+str(len(word_list))+"개의 어절이 사전에 등록되었습니다.")

    end = datetime.datetime.now()
    print("사전 구축 완료 ( " + str(end) + " )")
    print("===> 총 걸린 시간 : "+str(end-start))

def main():
    make_dict()

main()