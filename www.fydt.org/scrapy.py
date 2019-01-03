import bs4 as bs
import requests

res = requests.get('http://www.fydt.org/cat/shirenyushipian')


def parse_root_web_url_to_get_download_files(res):
    soup = bs.BeautifulSoup(res.text, features='lxml')
    elems = soup.select('a')
    for elem in elems:
        try:
            href_ = elem.attrs['href']
        except:
            pass
        if href_.find('mp3') > 0:
            # 'http://www.fydt.org/system/files_force/sermon/mobilepdf/Ps00_mobile.pdf?download=1'
            # elem.attrs['href']
            r = requests.get(href_)
            with open(elems[elems.index(elem)].attrs['title'], "wb") as code:
                # code.write(r.content)
                # break
                print(elems[elems.index(elem)].attrs['title'])
                print(href_)


parse_root_web_url_to_get_download_files(res)

playFile = open("""D:\\project\\ChristianTensor\\www.fydt.org\\download\\testPlayFileChild""", 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

print(type(res))
