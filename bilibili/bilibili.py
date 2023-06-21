import requests

class Bilibili:
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
            'Referer':'https://www.bilibili.com/v/popular/all/'
            # 'Cookie':"buvid3=8591163D-E0C2-AB81-7904-251C3C0749E364296infoc; b_nut=1684745064; b_lsid=A7F44428_1884647EFE9; _uuid=4EB66D2A-D16D-398F-D798-983DB3399D3F66658infoc; buvid_fp=4c5536d54d0d188c7985b7ad9a1c17d7; buvid4=3186A72A-C950-2702-A3B3-84D9D289807068341-023052216-idAyGdHccefBy/sgjD57lg%3D%3D; PVID=1; innersign=0; FEED_LIVE_VERSION=V_LIVE_1; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1542-505; CURRENT_FNVAL=4048; sid=qck47tk8; rpdid=|(k)muuYu|J|0J'uY)R)|YJm|"
            }

    def view(self, bvid: str):
        '''获得视频的元信息
        
        Args:
            bvid: 视频的bvid
            
        Returns:
            json object
        '''
        url = 'https://api.bilibili.com/x/web-interface/view'
        params = {
            'bvid': bvid
        }
        r = requests.get(url=url, headers=self.headers, params=params, timeout=10)
        r.encoding = 'utf-8'
        return r.json()
    
    def popular(self):
        '''获得热门视频列表

        Returns:
            json object
        '''
        url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
        r=requests.get(url=url, headers=self.headers, timeout=10)
        r.encoding='utf-8'
        return r.json()
    
