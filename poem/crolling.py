import urllib.request as req
import re
from bs4 import BeautifulSoup

url = "http://www.seelotus.com/gojeon/hyeon-dae/si/si-new/do-jong-hwan-n.htm#GlossA"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
poem_list = soup.select("dl")

saveFile = open("./poem03.txt","w",encoding="UTF-8")

# <class 'bs4.element.Tag'> 에서 <class 'str'> 으로 형변환
poem_list = map(str,poem_list)

line_list = []
# <br/> 을 \n으로 바꾸기
for line in poem_list:
    line_list.append(line.replace("<br/>", "\n"))

# \n\n이상인거 \n으로 모두 바꿔서 빈줄 너무 많은 거 없애기
temp_list= []
for l in line_list:
    temp_list.append(re.sub('[\n\n]+', '\n', l))

line_list = []
# 다시 html 방식으로 변환
# 거기서 텍스트 부분만 추출
for t in temp_list:
    line_list.append(BeautifulSoup(t,"html.parser").text)

for line in line_list:
    saveFile.write(line)

saveFile.close()