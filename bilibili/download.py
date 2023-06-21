import requests
import os

class VideoDownloader:
    def __init__(self, cid: int, avid: str = None, bvid: str = None, qn: int = 32) -> None:
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
            'Referer':'https://www.bilibili.com/v/popular/all/',
            'Cookie':"buvid3=8591163D-E0C2-AB81-7904-251C3C0749E364296infoc; b_nut=1684745064; b_lsid=A7F44428_1884647EFE9; _uuid=4EB66D2A-D16D-398F-D798-983DB3399D3F66658infoc; buvid_fp=4c5536d54d0d188c7985b7ad9a1c17d7; buvid4=3186A72A-C950-2702-A3B3-84D9D289807068341-023052216-idAyGdHccefBy/sgjD57lg%3D%3D; PVID=1; innersign=0; FEED_LIVE_VERSION=V_LIVE_1; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1542-505; CURRENT_FNVAL=4048; sid=qck47tk8; rpdid=|(k)muuYu|J|0J'uY)R)|YJm|"
            }
        self.avid = avid
        self.bvid = bvid
        self.metadata  = None
        self.qn = qn
        self.cid = cid
        self.save_dir = 'downloads'

        # 检查保存目录是否存在
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        if self.avid is not None:
            self.file_path = os.path.join(self.save_dir, f"{self.avid}.mp4")
        elif self.bvid is not None:
            self.file_path = os.path.join(self.save_dir, f"{self.bvid}.mp4")
        else:
            raise ValueError("avid or bvid must be specified")
    
    def get_metadata(self) -> None:
        '''获得视频的元信息
        Returns:
            json object
        '''
        params = {
            'avid': self.avid,
            'bvid': self.bvid,
            'cid': self.cid,
            'qn': self.qn,
        }
        base_url = f"https://api.bilibili.com/x/player/playurl"
        r = requests.get(url=base_url, headers=self.headers, params=params, timeout=10)
        r.encoding = 'utf-8'
        self.metadata = r.json()
    
    def download(self) -> str:
        '''下载视频
        Returns:
            file_path: str
        '''
        try:
            dash = self.metadata.get('data').get('dash')
            video_url = dash.get('video')[0].get('baseUrl')
            audio_url = dash.get('audio')[0].get('baseUrl')
            video = requests.get(url=video_url, headers=self.headers, timeout=10)
            audio = requests.get(url=audio_url, headers=self.headers, timeout=10)
            with open(self.file_path, 'wb') as f:
                f.write(video.content)
                f.write(audio.content)
        except:
            durl = self.metadata.get('data').get('durl')
            video_url = durl[0].get('url')
            video = requests.get(url=video_url, headers=self.headers, timeout=10)
            with open(self.file_path, 'wb') as f:
                f.write(video.content)
        # 返回文件的绝对路径
        return os.path.abspath(self.file_path)
