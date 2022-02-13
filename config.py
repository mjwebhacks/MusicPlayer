#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://eu10.fastcast4u.com/clubfmuae")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = 3796974
    CHAT = -1001597361595
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY="Y"
    ARQ_API="WPTSQF-OEAXKE-LEBXVB-ABAKYV-ARQ"
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    DURATION_LIMIT= 15
    DELAY = 10
    API_HASH = "9511d0112631f9990337eb724d1a7d0d"
    BOT_TOKEN = "5119166187:AAFtcwpmOwFHC3DSsm9W3qPUjIhFxdN-unA" 
    SESSION = "BQCo_i5B1NKstj_QpsK8p5gj9NM7TgnhoXhdILHMkofGqXumMrEs0TQamlQszj8Bo7FOTxp8XIaszx0qvu3W1QmFMxTAfQE26PBFvHfmfk9iZmmqBledBNNrm21ogQgZ7MyHi8d7PbbX-yre0CHmxiL4BWmgi7ZTLyknIgXmhoS04ExbzuvXwaYQntUNw7i-dq7J62cK3wdgWdUUaHdC6Hlyw9xODfwTrcBANeo_jqg1z6gWRbnFeKqzNdgdBXH7UvKjb-l9RedS1gchuz1syWwyVPLGl_1eabhFmJD9v5ZQRy5njU0Z9ahupFWS4pIfflN0l2k6S6IbPyjomAX2Wr5NV0PWxgA"
    playlist=[]
    msg = {}

