import re
import regex

# 파일 열기
originFile = open("./poem1.txt","r",encoding="UTF-8")
revisedFile = open("./poem01.txt","w",encoding="UTF-8")

# 개행문자 기준으로 끊어서 리스트화
origin_line = originFile.readlines()

# 수정 후의 문장들을 넣을 리스트
revised_line = []

p = re.compile('[-]+')

for line in origin_line:
    if line != '\n':
        revised_line.append(line)

origin_line = []

for line in revised_line:
    if p.match(line) == None:
        origin_line.append(line)

revised_line =[]

# [ 로 시작하는거 다 지우기
for line in origin_line :
    if line.startswith('[') or line.startswith(' ['):
        continue
    else :
        revised_line.append(line)

origin_line = []
# 문장 내에 있는 한문 모두 지우기
for line in revised_line :
    # line 안에 있는 모든 한문단어를 리스트(!)로 저장
    chinese = regex.findall('[\p{Han}]+',line)
    for c in chinese :
        line = line.replace(c,"")
    origin_line.append(line)

# 수정한 문장들을 파일에 출력
for line in origin_line:
    revisedFile.write(line)


originFile.close()
revisedFile.close()