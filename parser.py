import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req=requests.get('https://beomi.github.io/beomi.github.io_old/')


# HTML 소스 가져오기
html=req.text

'''
# HTTP Header 가져오기
header=req.headers

# HTTP Status 가져오기 (200: 정상)
status=req.status_code

#HTTP가 정상적으로 되었는지 (True/False)
is_ok=req.ok
'''
# BeautifulSoup으로 html소스를 python객체로 변환하기
# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시,
# 이 글에서는 Python 내장 html.parser를 이용.
soup=BeautifulSoup(html,'html.parser')

## CSS Selector를 통해 html 요소들을 찾아낸다.

my_titles=soup.select(
    'h3 > a'
)

## my_titles는 list 객체
for title in my_titles:
    ## Tag안의 텍스트
    print(title.text)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))