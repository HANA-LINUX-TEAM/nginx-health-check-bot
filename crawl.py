import os
import requests
from datetime import datetime

try:
    # index.html 전체 소스 가져오기
    res = requests.get(f"http://{os.environ['SERVER_IP']}/index.html", timeout=5)
    res.raise_for_status()
    html = res.text

    # Teams 메시지 길이 제한 고려해서 앞 1000자만 전송
    snippet = html[:1000]
    if len(html) > 1000:
        snippet += "\n... (이하 생략)"
except Exception as e:
    snippet = f"❌ 서버 응답 오류: {str(e)}"

# 메시지 구성
payload = {
    "text": f"**🌐 nginx index.html 전체 HTML 소스**\n\n- 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n```html\n{snippet}\n```"
}

# Webhook 전송
requests.post(os.environ["WEBHOOK_URL"], json=payload)
