from bilibili.bilibili import Bilibili
from bilibili.download import VideoDownloader

b = Bilibili()
# print(b.view('BV1ED4y1n7MD'))
# print(b.popular())

p = VideoDownloader(cid=975153366, avid='735654338')
p.get_metadata()
# print(p.metadata)
print(p.download())