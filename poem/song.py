from bs4 import BeautifulSoup
import urllib.request as req
import re

artistName="BTS"
writeTX = open("./"+artistName+".txt",'w',encoding="UTF-8")

artistId = 143179
url = "https://music.naver.com/artist/track.nhn?artistId="+str(artistId)
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

page_list = soup.select("#musicianHomePage > a")
page = len(page_list)
now = 0

b_list=[]
d_list=[]
for i in range(now,page):
    url_page = url+"&page="+str(i+1)
    res = req.urlopen(url_page)
    soup = BeautifulSoup(res, "html.parser")

    a_list = soup.select(
            "#content > div.mscn_wrap > div.mscn_ct > div.tracklist_area > div.tb_tracklst > table > tbody > tr > td.tb_name > span > a")

    c_list = soup.select("#content > div.mscn_wrap > div.mscn_ct > div.tracklist_area > div.tb_tracklst > table > tbody > tr > td.tb_lyrics > a")

    for i in range(0,len(a_list)):
        if "Inst." not in a_list[i].string:
            b_list.append(a_list[i].string)
            d_list.append(c_list[i].attrs['onclick'])

for d in d_list:
    trackId = re.findall(r"\d+",d)
    lyr_url = "https://music.naver.com/lyric/index.nhn?trackId="+str(trackId[0])
    res = req.urlopen(lyr_url)
    soup = BeautifulSoup(res, "html.parser")
    lyrics = soup.select("#pop_content > div.section_lyrics > div")

    for i in lyrics:
        writeTX.write(i.text + '\n')

writeTX.close()