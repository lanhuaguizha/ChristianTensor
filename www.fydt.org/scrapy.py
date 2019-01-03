from bs4 import BeautifulSoup
import requests

website_url = 'http://www.fydt.org/'
"""福音电台网站地址"""


def get_category_website_url(website_url):
    """获取网站目录地址"""
    req = requests.get(website_url)
    soup = BeautifulSoup(req.text, features='lxml')
    list_element_a = soup.find_all('li')
    for element_a in list_element_a:
        element_a.find_all('title')
        # 1.
        """<li class="first leaf"><a class="active" href="/" title="">首页</a></li>"""
        """<li class="expanded"><a href="/cat/zhuantixilie" title="专题系列">专题系列</a><ul class="menu"><li class="first leaf"><a href="/cat/shirenyushipian" title="">诗人与诗篇</a></li>
<li class="leaf"><a href="http://www.fydt.org/cat/xili" title="洗礼">洗礼</a></li>
<li class="leaf"><a href="/cat/jidutuhunyin" title="基督徒婚姻">基督徒婚姻</a></li>
<li class="leaf"><a href="/cat/shengdanjie" title="圣诞节">圣诞节</a></li>
<li class="leaf"><a href="/cat/nonglixinnian" title="农历新年">农历新年</a></li>
<li class="leaf"><a href="/cat/shengjingrenwu" title="圣经人物">圣经人物</a></li>
<li class="leaf"><a href="/cat/fuyin" title="福音">福音</a></li>
<li class="leaf"><a href="/cat/fuhuojie" title="复活节">复活节</a></li>
<li class="leaf"><a href="/cat/xinshengming" title="新生命">新生命</a></li>
<li class="last leaf"><a href="/cat/zuoshenxiyuedepuren" title="作神喜悦的仆人">作神喜悦的仆人</a></li>
</ul></li>"""
        """<li class="first leaf"><a href="/cat/shirenyushipian" title="">诗人与诗篇</a></li>"""
        """<li class="leaf"><a href="http://www.fydt.org/cat/xili" title="洗礼">洗礼</a></li>"""
        """<li class="leaf"><a href="/cat/jidutuhunyin" title="基督徒婚姻">基督徒婚姻</a></li>"""
        """<li class="leaf"><a href="/cat/shengdanjie" title="圣诞节">圣诞节</a></li>"""
        """<li class="leaf"><a href="/cat/nonglixinnian" title="农历新年">农历新年</a></li>"""
        """..."""
        """<li class="last leaf"><a href="/cat/zuoshenxiyuedepuren" title="作神喜悦的仆人">作神喜悦的仆人</a></li>"""

        # 2.
        """<li class="expanded"><a href="/cat/jiangdaoxinxi" title="讲道信息">讲道信息</a><ul class="menu"><li class="first leaf"><a href="/cat/xunqiushendezhengquetujing" title="寻求神的正确途径">寻求神的正确途径</a></li>
<li class="leaf"><a href="/cat/zongjiaoyushulingdeduibi" title="宗教与属灵的对比">宗教与属灵的对比</a></li>
<li class="leaf"><a href="/cat/shengmingdezhenyan" title="生命的箴言">生命的箴言</a></li>
<li class="leaf"><a href="/cat/shengmingsuzhi" title="生命素质">生命素质</a></li>
<li class="leaf"><a href="/cat/zhuanruoweineng" title="转弱为能">转弱为能</a></li>
<li class="last leaf"><a href="/cat/dulixinxi" title="独立信息">独立信息</a></li>
</ul></li>"""
        """<li class="first leaf"><a href="/cat/xunqiushendezhengquetujing" title="寻求神的正确途径">寻求神的正确途径</a></li>"""
        """<li class="leaf"><a href="/cat/zongjiaoyushulingdeduibi" title="宗教与属灵的对比">宗教与属灵的对比</a></li>"""
        """..."""

        # 3.
        """<li class="expanded"><a href="/cat/shujuanchakao" title="书卷查考">书卷查考</a><ul class="menu"><li class="first leaf"><a href="/cat/chuangshiji" title="创世记漫谈">创世记</a></li>
<li class="leaf"><a href="/cat/liewangjishang" title="列王纪上">列王纪上</a></li>
<li class="leaf"><a href="http://www.fydt.org/cat/zhenyan" title="">箴言</a></li>
<li class="leaf"><a href="/cat/mataifuyin" title="马太福音">马太福音</a></li>
<li class="leaf"><a href="/cat/luomashuzonglan" title="罗马书纵览">罗马书(纵览)</a></li>
<li class="leaf"><a href="/cat/luomashu" title="罗马书">罗马书</a></li>
<li class="leaf"><a href="http://www.fydt.org/cat/gelinduoqianshu" title="哥林多前书">哥林多前书</a></li>
<li class="leaf"><a href="/cat/feilibishu" title="腓立比书">腓立比书</a></li>
<li class="leaf"><a href="/cat/yageshu" title="雅各书">雅各书</a></li>
<li class="leaf"><a href="/cat/bideqianshu" title="彼得前书">彼得前书</a></li>
<li class="leaf"><a href="/cat/bidehoushu" title="彼得后书">彼得后书</a></li>
<li class="leaf"><a href="/cat/yuehanyishu" title="约翰一书">约翰一书</a></li>
<li class="last leaf"><a href="/cat/youdashu" title="犹大书">犹大书</a></li>
</ul></li>"""
        """<li class="first leaf"><a href="/cat/chuangshiji" title="创世记漫谈">创世记</a></li>"""

        # 4.
        """<li class="leaf"><a href="/cat/shengjingyishenlun" title="圣经一神论">圣经一神论</a></li>"""

        # 5.
        """<li class="leaf"><a href="/cat/qimiaoendian0" title="奇妙恩典">奇妙恩典</a></li>"""

        # 6.
        """<li class="leaf"><a href="/cat/shengmingzaisi" title="生命再思">生命再思</a></li>"""

        # 7.（无需）
        """<li class="leaf"><a href="/faq" title="">专题解答</a></li>"""

        # 8.（无需）
        """。。。"""

        print(element_a)


get_category_website_url(website_url)

# res = requests.get('http://www.fydt.org/cat/shirenyushipian')
#
#
# def parse_root_web_url_to_get_download_files(res):
#     soup = bs.BeautifulSoup(res.text, features='lxml')
#     elems = soup.select('a')
#     for elem in elems:
#         try:
#             href_ = elem.attrs['href']
#         except:
#             pass
#         if href_.find('mp3') > 0:
#             # 'http://www.fydt.org/system/files_force/sermon/mobilepdf/Ps00_mobile.pdf?download=1'
#             # elem.attrs['href']
#             r = requests.get(href_)
#             with open('01', "wb") as code:
#                 code.write(r.content)
#                 break
#                 # print(elems[elems.index(elem)].attrs['title'])
#                 # print(href_)
#
#
# parse_root_web_url_to_get_download_files(res)
#
# playFile = open("""D:\\project\\ChristianTensor\\www.fydt.org\\download\\testPlayFileChild""", 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
#
# print(type(res))
