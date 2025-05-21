# crawl.py
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

try:
    res = requests.get(f"http://{os.environ['SERVER_IP']}/index.html", timeout=5)
    if res.status_code != 200:
        raise Exception(f"응답 코드: {res.status_code}")
    soup = BeautifulSoup(res.text, "html.parser")
    info = soup.find("h1")
    text = info.text.strip() if info else "(<h1> 없음)"
except Exception as e:
    text = f"❌ 서버 응답 오류: {str(e)}"

payload = {
    "text": f"**🌐 nginx 서버 index.html 상태**\n\n- 내용: {text}\n- 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
}

requests.post(os.environ["WEBHOOK_URL"], json=payload)
