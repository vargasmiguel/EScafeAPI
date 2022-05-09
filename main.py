from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import urllib.request
import ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/{day}")
def prices(day: str):
    day2=day.split('-')
    day3=str(int(day2[0])-1).zfill(2)+'/'+day2[1]+'/'+day2[2]
    req = urllib.request.Request(f'https://www.cccv.org.br/includes/ajaxDay.php?dt_cotacao={day3}', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    page = urllib.request.urlopen(req)
    charset=page.info().get_content_charset()
    content=page.read().decode(charset)
    bs = BeautifulSoup(content)
    data = bs.findAll(lambda tag: tag.name=='p')
    data=[x.text for x in data]
    daytxt= bs.findAll(lambda tag: tag.name=='h1')[2].text.split(' ')[0]
    if len(data)<13 or daytxt!=(str(int(day2[0])).zfill(2)):
        return {'error': 'No data for this day'}
    else:
        return {'arabica-dura-2021/2022':data[3], 'arabica-dura-2022/2023':data[4], 'arabica-rio-2021/2022':data[6], 'arabica-rio-2022/2023':data[7], 'conilon-2021/2022':data[11], 'conilon-2022/2023':data[12]}    

    
@app.get("/month/")
def month():
    req = urllib.request.Request(f'https://www.cccv.org.br/cotacao/', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    page = urllib.request.urlopen(req)
    charset=page.info().get_content_charset()
    content=page.read().decode(charset)
    bs = BeautifulSoup(content)
    data = bs.findAll(lambda tag: tag.name=='td')
    data=[x.text for x in data]
    data2=data[12:-1]
    resp={}
    for i in range(0, len(data2), 7):
        resp[data2[i]] = {'arabica-dura-2021/2022':data2[i+1], 'arabica-rio-2021/2022':data2[i+2], 'arabica-dura-2022/2023':data2[i+3], 'arabica-rio-2022/2023':data2[i+4], 'conilon-2021/2022':data2[i+5], 'conilon-2022/2023':data2[i+6]}
    return resp
