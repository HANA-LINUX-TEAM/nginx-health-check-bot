import os
import requests
from datetime import datetime

try:
    res = requests.get(f"http://{os.environ['SERVER_IP']}/index.html", timeout=5)
    if res.status_code != 200:
        raise Exception(f"응답 코드: {res.status_code}")
    html = res.text
    # 긴 메시지는 자르기 (예: 앞부분 500자)
    html_snippet = html[:500] + ("..." if len(html) > 500 else "")
except Exception as e:
    html_snippet = f"❌ 서버 응답 오류: {str(e)}"

payload = {
    "text": f"**🌐 index.html 전체 내용 확인**\n\n시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n```html\n{html_snippet}\n```"
}

requests.post(os.environ["WEBHOOK_URL"], json=payload)
