from bs4 import BeautifulSoup
from urllib import request
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <h1>Hello External Modual 수프</h1>
# <h1>Hello External Modual 수프2</h1>
# <h1>Hello External Modual 수프3</h1>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')   # 객체 생성과 동시에 초기화 'html.parser을 이용해 초기화 
# #print(soup.prettify())

# print(soup.find_all('h1'))

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(target,"html.parser")

for loca in soup.select("location"):
    print("날짜 : ", loca.select_one("tmEf").string)
    print("도시 : ", loca.select_one("city").string)
    print("날씨 : ", loca.select_one("wf").string)
    print("최저기온 : ", loca.select_one("tmn").string)
    print("최고기온 : ", loca.select_one("tmx").string)    
    print("----------------------------------------")
    #print(type(loca))



